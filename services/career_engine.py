# services/career_engine.py
import json
import random
from datetime import date, datetime, timedelta
from database import db
from models.university import CareerPath, CareerStage, QuizQuestion, CareerProgress


class CareerEngine:
    """محرك إدارة المسارات المهنية"""

    # ==========================================
    # XP Calculator
    # ==========================================
    XP_FIRST_TRY = 100        # نجاح من المحاولة الأولى
    XP_SECOND_TRY = 70        # نجاح من المحاولة الثانية
    XP_THIRD_TRY = 50         # نجاح من الثالثة فما فوق
    XP_COMPLETE_PATH = 500    # مكافأة إكمال المسار كاملاً

    # ==========================================
    # 1. توليد اختبار عشوائي
    # ==========================================
    @staticmethod
    def generate_quiz(stage_id, num_questions=10):
        """
        توليد اختبار عشوائي من بنك الأسئلة.
        - يختار num_questions عشوائياً من بنك المرحلة.
        - يعيد قائمة بالأسئلة (بدون الإجابة الصحيحة).
        """
        all_questions = QuizQuestion.query.filter_by(stage_id=stage_id).all()

        if len(all_questions) < num_questions:
            num_questions = len(all_questions)

        selected = random.sample(all_questions, num_questions)

        # خلط الخيارات داخل كل سؤال (لإعطاء ترتيب مختلف في كل محاولة)
        quiz_data = []
        for q in selected:
            options = q.get_options()
            # خلط ترتيب الخيارات
            option_items = list(options.items())  # [('A', '...'), ('B', '...')]
            random.shuffle(option_items)

            # إعادة تعيين الحروف بعد الخلط
            new_options = {}
            option_map = {}  # لتتبع الإجابة الصحيحة بعد الخلط
            letters = ['A', 'B', 'C', 'D']

            for i, (old_key, text) in enumerate(option_items):
                new_key = letters[i]
                new_options[new_key] = text
                if old_key == q.correct_answer:
                    option_map['correct'] = new_key

            quiz_data.append({
                'id': q.id,
                'text': q.question_text,
                'options': new_options,
                'difficulty': q.difficulty,
                'correct': option_map.get('correct', q.correct_answer)  # للتصحيح الداخلي
            })

        return quiz_data

    # ==========================================
    # 2. تصحيح الاختبار
    # ==========================================
    @staticmethod
    def grade_quiz(quiz_data, user_answers):
        """
        تصحيح إجابات المستخدم.
        - quiz_data: قائمة الأسئلة (مع 'correct').
        - user_answers: {question_id: 'A'/'B'/'C'/'D'}.
        - يعيد dict: {score, total, passed, details}.
        """
        score = 0
        total = len(quiz_data)
        details = []

        for q in quiz_data:
            q_id = str(q['id'])
            user_answer = user_answers.get(q_id)
            is_correct = (user_answer == q['correct'])

            if is_correct:
                score += 1

            details.append({
                'question_id': q['id'],
                'user_answer': user_answer,
                'correct_answer': q['correct'],
                'is_correct': is_correct
            })

        passed = (score >= 11)  # 70% من 15 تقريباً = 11
        # لكن المستخدم يرى 10 أسئلة، لذا المعيار:
        # 7 من 10 = 70%
        passed = (score >= 7) if total == 10 else (score / total >= 0.7)

        return {
            'score': score,
            'total': total,
            'passed': passed,
            'details': details
        }

    # ==========================================
    # 3. حساب XP
    # ==========================================
    @staticmethod
    def calculate_xp(progress, stage_number, attempts_count):
        """
        حساب XP بناءً على عدد المحاولات.
        - attempts_count: عدد المحاولات لهذه المرحلة (1, 2, 3...).
        """
        if attempts_count == 1:
            return CareerEngine.XP_FIRST_TRY
        elif attempts_count == 2:
            return CareerEngine.XP_SECOND_TRY
        else:
            return CareerEngine.XP_THIRD_TRY

    # ==========================================
    # 4. إدارة Streak
    # ==========================================
    @staticmethod
    def update_streak(progress):
        """
        تحديث Streak (الأيام المتتالية).
        - إذا كان آخر نشاط اليوم → لا تغيير.
        - إذا كان آخر نشاط أمس → +1.
        - إذا أكثر من يوم → إعادة تعيين إلى 1.
        """
        today = date.today()

        if progress.last_streak_date == today:
            return  # نفس اليوم، لا تغيير

        if progress.last_streak_date == today - timedelta(days=1):
            progress.streak_days += 1
        else:
            progress.streak_days = 1  # بداية جديدة

        progress.last_streak_date = today

    # ==========================================
    # 5. حفظ نتيجة اختبار
    # ==========================================
    @staticmethod
    def save_quiz_attempt(user_id, career_path_id, stage_number, score, total, passed):
        """
        حفظ محاولة اختبار في قاعدة البيانات.
        - يحدّث progress (attempts, XP, current_stage, completed_stages).
        """
        # جلب أو إنشاء progress
        progress = CareerProgress.query.filter_by(
            user_id=user_id,
            career_path_id=career_path_id
        ).first()

        if not progress:
            progress = CareerProgress(
                user_id=user_id,
                career_path_id=career_path_id,
                current_stage=1
            )
            db.session.add(progress)
            db.session.flush()

        # جلب المحاولات السابقة
        attempts = progress.get_attempts()
        stage_key = str(stage_number)
        if stage_key not in attempts:
            attempts[stage_key] = []

        attempts[stage_key].append({
            'score': score,
            'total': total,
            'passed': passed,
            'date': datetime.utcnow().isoformat()
        })

        progress.attempts = json.dumps(attempts, ensure_ascii=False)
        progress.last_activity = datetime.utcnow()

        # تحديث Streak
        CareerEngine.update_streak(progress)

        # إذا نجح → تحديث المراحل المكتملة + XP
        if passed:
            completed = progress.get_completed_stages()
            if stage_number not in completed:
                completed.append(stage_number)
                progress.completed_stages = json.dumps(completed)

                # حساب XP
                attempt_count = len(attempts[stage_key])
                xp = CareerEngine.calculate_xp(progress, stage_number, attempt_count)
                progress.total_xp += xp

            # تحديث المرحلة الحالية
            career_path = CareerPath.query.get(career_path_id)
            if stage_number >= progress.current_stage:
                if stage_number < career_path.total_stages:
                    progress.current_stage = stage_number + 1

            # فحص إكمال المسار
            if len(completed) >= career_path.total_stages:
                if not progress.is_completed:
                    progress.is_completed = True
                    progress.completed_at = datetime.utcnow()
                    progress.total_xp += CareerEngine.XP_COMPLETE_PATH

        db.session.commit()
        return progress

    # ==========================================
    # 6. جلب/إنشاء progress للمستخدم
    # ==========================================
    @staticmethod
    def get_or_create_progress(user_id, career_path_id):
        """جلب progress الموجود أو إنشاء جديد"""
        progress = CareerProgress.query.filter_by(
            user_id=user_id,
            career_path_id=career_path_id
        ).first()

        if not progress:
            progress = CareerProgress(
                user_id=user_id,
                career_path_id=career_path_id,
                current_stage=1
            )
            db.session.add(progress)
            db.session.commit()

        return progress

    # ==========================================
    # 7. فحص فتح المرحلة
    # ==========================================
    @staticmethod
    def is_stage_unlocked(progress, stage_number):
        """
        فحص إذا كانت المرحلة مفتوحة.
        - المرحلة 1 دائماً مفتوحة.
        - المرحلة N مفتوحة إذا أُكملت N-1.
        """
        if stage_number == 1:
            return True

        completed = progress.get_completed_stages()
        return (stage_number - 1) in completed

    # ==========================================
    # 8. جلب حالة المسار كاملة
    # ==========================================
    @staticmethod
    def get_path_status(user_id, career_path_id):
        """
        إرجاع dict بحالة المسار للمستخدم:
        - progress
        - stages_status (لكل مرحلة: unlocked/completed)
        - percentage
        """
        career_path = CareerPath.query.get(career_path_id)
        if not career_path:
            return None

        progress = CareerEngine.get_or_create_progress(user_id, career_path_id)
        completed = progress.get_completed_stages()

        stages_status = []
        for stage in career_path.stages:
            stages_status.append({
                'stage': stage,
                'is_completed': stage.stage_number in completed,
                'is_unlocked': CareerEngine.is_stage_unlocked(progress, stage.stage_number),
                'is_current': stage.stage_number == progress.current_stage
            })

        return {
            'career_path': career_path,
            'progress': progress,
            'stages_status': stages_status,
            'percentage': progress.get_progress_percentage(),
            'completed_count': len(completed),
            'total_stages': career_path.total_stages
        }