# data/seed_careers.py
"""
Script لإدخال محتوى المسارات المهنية في قاعدة البيانات.
يُشغَّل مرة واحدة فقط بعد تعريف الجداول.
"""

import json
from database import db
from models.university import CareerPath, CareerStage, QuizQuestion
from data.career_content_da import DATA_SCIENCE_PATHS
from data.career_content_ds import DATA_SCIENTIST_PATHS    # ← يجب أن يكون هنا
from data.career_content_de import DATA_ENGINEER_PATHS
from data.career_content_ml import ML_ENGINEER_PATHS
from data.career_content_cv import CV_ENGINEER_PATHS
from data.career_content_nlp import NLP_ENGINEER_PATHS
from data.career_content_security import SECURITY_ANALYST_PATHS
from data.career_content_pentest import PENETRATION_TESTER_PATHS
from data.career_content_netsec import NETWORK_SECURITY_PATHS





def seed_career_path(path_data):
    """يُدخل مسار مهني واحد + مراحله + أسئلته"""
    
    # 1. تحقق من عدم وجود المسار مسبقاً
    existing = CareerPath.query.filter_by(slug=path_data['slug']).first()
    if existing:
        print(f"⏩ المسار '{path_data['slug']}' موجود بالفعل، سيتم تحديثه...")
        # احذف المراحل القديمة (Cascade يحذف الأسئلة)
        CareerStage.query.filter_by(career_path_id=existing.id).delete()
        db.session.commit()
        career_path = existing
    else:
        # 2. أنشئ المسار الجديد
        career_path = CareerPath(
            major_key=path_data['major_key'],
            slug=path_data['slug'],
            title=path_data['title'],
            description=path_data['description'],
            icon=path_data['icon'],
            difficulty=path_data['difficulty'],
            estimated_hours=path_data['estimated_hours'],
            order_index=path_data.get('order_index', 0)
        )
        db.session.add(career_path)
        db.session.flush()  # للحصول على ID

    # 3. أضف المراحل والأسئلة
    total_stages = 0
    total_questions = 0

    for stage_data in path_data['stages']:
        stage = CareerStage(
            career_path_id=career_path.id,
            stage_number=stage_data['stage_number'],
            title=stage_data['title'],
            description=stage_data['description'],
            objectives=json.dumps(stage_data['objectives'], ensure_ascii=False),
            practical_task=stage_data['practical_task'],
            youtube_ar=stage_data.get('youtube_ar', ''),
            youtube_en=stage_data.get('youtube_en', ''),
            passing_score=11,  # 11/15 = 73%
            total_quiz_questions=10  # عرض 10 أسئلة عشوائية
        )
        db.session.add(stage)
        db.session.flush()  # للحصول على ID

        # 4. أضف أسئلة المرحلة
        for q_data in stage_data['questions']:
            question = QuizQuestion(
                stage_id=stage.id,
                question_text=q_data['text'],
                options=json.dumps(q_data['options'], ensure_ascii=False),
                correct_answer=q_data['correct'],
                difficulty=q_data.get('difficulty', 'easy')
            )
            db.session.add(question)
            total_questions += 1

        total_stages += 1
        print(f"   ✅ المرحلة {stage_data['stage_number']}: {stage_data['title']} ({len(stage_data['questions'])} سؤال)")

    # 5. حدّث عدد المراحل
    career_path.total_stages = total_stages

    return total_stages, total_questions



def seed_all_careers():
    """يُدخل كل المسارات المتاحة"""
    all_paths = (
        DATA_SCIENCE_PATHS +
        DATA_SCIENTIST_PATHS +
        DATA_ENGINEER_PATHS +
        ML_ENGINEER_PATHS +
        CV_ENGINEER_PATHS +
        NLP_ENGINEER_PATHS  +
        SECURITY_ANALYST_PATHS +
        PENETRATION_TESTER_PATHS  +
        NETWORK_SECURITY_PATHS 
    )  # لاحقاً: أضف AI_PATHS + CYBER_PATHS

    print("=" * 60)
    print("🌱 بدء إدخال المسارات المهنية...")
    print("=" * 60)

    total_paths_count = 0
    total_stages_count = 0
    total_questions_count = 0

    for path_data in all_paths:
        print(f"\n📊 معالجة المسار: {path_data['title']}")
        stages, questions = seed_career_path(path_data)
        total_paths_count += 1
        total_stages_count += stages
        total_questions_count += questions

    db.session.commit()

    print("\n" + "=" * 60)
    print("✅ اكتمل الإدخال بنجاح!")
    print("=" * 60)
    print(f"📊 المسارات المُدخلة: {total_paths_count}")
    print(f"📚 المراحل المُدخلة: {total_stages_count}")
    print(f"❓ الأسئلة المُدخلة: {total_questions_count}")
    print("=" * 60)


if __name__ == '__main__':
    seed_all_careers()