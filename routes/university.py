# routes/university.py
from flask import Blueprint, render_template, request, redirect, url_for, session, flash, jsonify
from utils.decorators import login_required
from models.user import User
from models.university import (
    UniversityProfile, CareerPath, CareerStage,
    QuizQuestion, CareerProgress
)
from services.career_engine import CareerEngine
from database import db
import json


university_bp = Blueprint('university', __name__)


AVAILABLE_MAJORS = [
    {'key': 'data_science', 'name': 'علوم البيانات', 'icon': '📊'},
    {'key': 'ai', 'name': 'الذكاء الاصطناعي', 'icon': '🤖'},
    {'key': 'cyber', 'name': 'الأمن السيبراني', 'icon': '🔒'},
]


# ==========================================
# 1. الصفحة الرئيسية (Home) - اختيار التخصص والمسار
# ==========================================
@university_bp.route('/setup', methods=['GET'])
@login_required
def setup():
    user_id = session['user_id']
    user = User.query.get(user_id)

    uni_profile = UniversityProfile.query.filter_by(user_id=user_id).first()

    return render_template(
        'university/setup.html',
        user=user,
        uni_profile=uni_profile,
        majors=AVAILABLE_MAJORS,
        current_tab='home'
    )


# ==========================================
# 2. حفظ اختيار التخصص + المسار
# ==========================================
@university_bp.route('/setup', methods=['POST'])
@login_required
def save_setup():
    user_id = session['user_id']
    user = User.query.get(user_id)

    major = request.form.get('major')
    preferred_track = request.form.get('preferred_track')

    if not major or not preferred_track:
        flash('يرجى اختيار التخصص والمسار المفضل', 'danger')
        return redirect(url_for('university.setup'))

    # ✅ تحديث أو إنشاء UniversityProfile
    uni_profile = UniversityProfile.query.filter_by(user_id=user_id).first()
    if not uni_profile:
        uni_profile = UniversityProfile(user_id=user_id)
        db.session.add(uni_profile)

    uni_profile.major = major
    uni_profile.preferred_track = preferred_track
    user.user_type = 'university'

    # ✅ البحث عن المسار
    career_path = CareerPath.query.filter_by(slug=preferred_track).first()
    if not career_path:
        db.session.commit()
        flash('لم يُعثر على المسار المطلوب', 'danger')
        return redirect(url_for('university.dashboard'))

    # ✅ إنشاء CareerProgress إذا لم يوجد
    existing_progress = CareerProgress.query.filter_by(
        user_id=user_id,
        career_path_id=career_path.id
    ).first()

    if not existing_progress:
        new_progress = CareerProgress(
            user_id=user_id,
            career_path_id=career_path.id,
            current_stage=1
        )
        db.session.add(new_progress)

    db.session.commit()
    flash(f'✅ تم تفعيل المسار: {career_path.title}', 'success')
    return redirect(url_for('university.dashboard', track=career_path.slug))


# ==========================================
# 3. Dashboard - مع Tabs للمسارات
# ==========================================
@university_bp.route('/dashboard')
@login_required
def dashboard():
    user_id = session['user_id']
    user = User.query.get(user_id)

    uni_profile = UniversityProfile.query.filter_by(user_id=user_id).first()
    if not uni_profile:
        return redirect(url_for('university.setup'))

    # جلب جميع مسارات المستخدم
    progress_list = CareerProgress.query.filter_by(user_id=user_id).all()

    # إذا لم يبدأ أي مسار → Empty State
    if not progress_list:
        return render_template(
            'university/dashboard.html',
            user=user,
            uni_profile=uni_profile,
            total_xp=0,
            current_streak=0,
            active_paths=0,
            completed_paths=0,
            current_path_status=None,
            progress_list=[],
            current_slug=None,
            current_tab='dashboard'
        )

    # ✅ تحديد المسار المطلوب من URL
    requested_slug = request.args.get('track')

    if requested_slug:
        current_progress = next(
            (p for p in progress_list if p.career_path.slug == requested_slug),
            None
        )
        if not current_progress:
            current_progress = max(progress_list, key=lambda p: p.last_activity or 0)
    else:
        # آخر مسار نشاطاً
        current_progress = max(progress_list, key=lambda p: p.last_activity or 0)

    # جلب حالة المسار الحالي
    current_path_status = CareerEngine.get_path_status(user_id, current_progress.career_path_id)

    # إحصائيات عامة
    total_xp = sum(p.total_xp for p in progress_list)
    current_streak = max([p.streak_days for p in progress_list] or [0])
    completed_paths = sum(1 for p in progress_list if p.is_completed)
    active_paths = len([p for p in progress_list if not p.is_completed])

    return render_template(
        'university/dashboard.html',
        user=user,
        uni_profile=uni_profile,
        total_xp=total_xp,
        current_streak=current_streak,
        completed_paths=completed_paths,
        active_paths=active_paths,
        current_path_status=current_path_status,
        progress_list=progress_list,
        current_slug=current_progress.career_path.slug,
        current_tab='dashboard'
    )


# ==========================================
# 4. صفحة المسار (المراحل)
# ==========================================
@university_bp.route('/career/<path_slug>')
@login_required
def career_path(path_slug):
    user_id = session['user_id']
    user = User.query.get(user_id)

    career_path_obj = CareerPath.query.filter_by(slug=path_slug).first()
    if not career_path_obj:
        flash('المسار غير موجود', 'danger')
        return redirect(url_for('university.dashboard'))

    status = CareerEngine.get_path_status(user_id, career_path_obj.id)

    return render_template(
        'university/career_path.html',
        user=user,
        status=status,
        career_path=career_path_obj
    )


# ==========================================
# 5. صفحة المرحلة (الدرس)
# ==========================================
@university_bp.route('/stage/<int:stage_id>')
@login_required
def stage_detail(stage_id):
    user_id = session['user_id']
    user = User.query.get(user_id)

    stage = CareerStage.query.get_or_404(stage_id)
    career_path_obj = CareerPath.query.get(stage.career_path_id)

    progress = CareerEngine.get_or_create_progress(user_id, career_path_obj.id)
    if not CareerEngine.is_stage_unlocked(progress, stage.stage_number):
        flash('هذه المرحلة مقفلة. أكمل المرحلة السابقة أولاً.', 'warning')
        return redirect(url_for('university.career_path', path_slug=career_path_obj.slug))

    return render_template(
        'university/stage.html',
        user=user,
        stage=stage,
        career_path=career_path_obj,
        objectives=stage.get_objectives()
    )


# ==========================================
# 6. صفحة الاختبار
# ==========================================
@university_bp.route('/quiz/<int:stage_id>')
@login_required
def quiz(stage_id):
    user_id = session['user_id']
    user = User.query.get(user_id)

    stage = CareerStage.query.get_or_404(stage_id)
    career_path_obj = CareerPath.query.get(stage.career_path_id)

    progress = CareerEngine.get_or_create_progress(user_id, career_path_obj.id)
    if not CareerEngine.is_stage_unlocked(progress, stage.stage_number):
        flash('هذه المرحلة مقفلة.', 'warning')
        return redirect(url_for('university.career_path', path_slug=career_path_obj.slug))

    quiz_data = CareerEngine.generate_quiz(stage.id, num_questions=10)

    # تخزين الأسئلة في session للتصحيح
    session[f'quiz_{stage.id}'] = [
        {'id': q['id'], 'correct': q['correct']}
        for q in quiz_data
    ]

    return render_template(
        'university/quiz.html',
        user=user,
        stage=stage,
        career_path=career_path_obj,
        quiz_data=quiz_data
    )


# ==========================================
# 7. تصحيح الاختبار
# ==========================================
@university_bp.route('/quiz/<int:stage_id>/submit', methods=['POST'])
@login_required
def quiz_submit(stage_id):
    user_id = session['user_id']

    stage = CareerStage.query.get_or_404(stage_id)
    career_path_obj = CareerPath.query.get(stage.career_path_id)

    stored_quiz = session.get(f'quiz_{stage.id}', [])
    if not stored_quiz:
        flash('انتهت صلاحية الاختبار. يرجى إعادة الدخول.', 'warning')
        return redirect(url_for('university.quiz', stage_id=stage.id))

    user_answers = {}
    for q in stored_quiz:
        answer = request.form.get(f'question_{q["id"]}')
        if answer:
            user_answers[str(q['id'])] = answer

    quiz_data_for_grading = [
        {'id': q['id'], 'correct': q['correct']}
        for q in stored_quiz
    ]

    result = CareerEngine.grade_quiz(quiz_data_for_grading, user_answers)

    CareerEngine.save_quiz_attempt(
        user_id=user_id,
        career_path_id=career_path_obj.id,
        stage_number=stage.stage_number,
        score=result['score'],
        total=result['total'],
        passed=result['passed']
    )

    session[f'quiz_result_{stage.id}'] = result
    session.pop(f'quiz_{stage.id}', None)

    return redirect(url_for('university.quiz_result', stage_id=stage.id))


# ==========================================
# 8. صفحة النتيجة
# ==========================================
@university_bp.route('/quiz/<int:stage_id>/result')
@login_required
def quiz_result(stage_id):
    user_id = session['user_id']
    user = User.query.get(user_id)

    stage = CareerStage.query.get_or_404(stage_id)
    career_path_obj = CareerPath.query.get(stage.career_path_id)

    result = session.pop(f'quiz_result_{stage.id}', None)
    if not result:
        flash('لا توجد نتيجة لعرضها.', 'warning')
        return redirect(url_for('university.career_path', path_slug=career_path_obj.slug))

    status = CareerEngine.get_path_status(user_id, career_path_obj.id)

    return render_template(
        'university/quiz_result.html',
        user=user,
        stage=stage,
        career_path=career_path_obj,
        result=result,
        status=status
    )


# ==========================================
# 9. بدء مسار جديد (API)
# ==========================================
@university_bp.route('/career/<int:path_id>/start', methods=['POST'])
@login_required
def start_career(path_id):
    user_id = session['user_id']
    career_path_obj = CareerPath.query.get_or_404(path_id)

    CareerEngine.get_or_create_progress(user_id, career_path_obj.id)
    flash(f'تم بدء مسار: {career_path_obj.title}', 'success')
    return redirect(url_for('university.career_path', path_slug=career_path_obj.slug))


# ==========================================
# 10. تغيير التخصص (يرجع لـ Home)
# ==========================================
@university_bp.route('/change-major')
@login_required
def change_major():
    user_id = session['user_id']
    user = User.query.get(user_id)

    # لا نحذف أي شيء — فقط نوجه لـ Home
    user.user_type = 'university'
    db.session.commit()

    return redirect(url_for('university.setup'))
# ==========================================
# 11. حذف مسار المستخدم
# ==========================================
@university_bp.route('/career/<path_slug>/delete', methods=['POST'])
@login_required
def delete_career(path_slug):
    user_id = session['user_id']
    
    career_path_obj = CareerPath.query.filter_by(slug=path_slug).first()
    if not career_path_obj:
        flash('المسار غير موجود', 'danger')
        return redirect(url_for('university.dashboard'))
    
    # حذف تقدم المستخدم في هذا المسار فقط
    progress = CareerProgress.query.filter_by(
        user_id=user_id,
        career_path_id=career_path_obj.id
    ).first()
    
    if progress:
        db.session.delete(progress)
        db.session.commit()
        flash(f'✅ تم حذف مسار: {career_path_obj.title}', 'success')
    else:
        flash('لا يوجد تقدم لحذفه في هذا المسار', 'warning')
    
    return redirect(url_for('university.dashboard'))