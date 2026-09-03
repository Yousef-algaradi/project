# routes/student.py
from flask import Blueprint, render_template, request, redirect, url_for, session, flash, jsonify
from utils.decorators import login_required
from models.user import User, AssessmentResult
from models.high_school import HighSchoolProfile
from models.recommendation import Recommendation
from services.analysis_engine import AnalysisEngine
from services.assessment_engine import AssessmentEngine

from database import db
import json

student_bp = Blueprint('student', __name__)

# ========== عرض صفحة اختبار الميول ==========
@student_bp.route('/assessment')
@login_required
def assessment():
    # جلب أسئلة الاختبار من AssessmentEngine
    questions = AssessmentEngine.QUESTIONS
    return render_template('assessment.html', questions=questions)

# ========== استقبال نتائج اختبار الميول ==========
@student_bp.route('/assessment/submit', methods=['POST'])
@login_required
def submit_assessment():
    user_id = session['user_id']
    data = request.get_json()
    if not data:
        return jsonify({'error': 'لا توجد بيانات'}), 400

    answers = data.get('answers', {})  # {question_id: option_id}
    # حساب درجات الأبعاد
    scores = AssessmentEngine.calculate_dimension_scores(answers)

    # حفظ أو تحديث نتيجة المستخدم في قاعدة البيانات
    result = AssessmentResult.query.filter_by(user_id=user_id).first()
    if not result:
        result = AssessmentResult(user_id=user_id)
        db.session.add(result)

    result.aptitude_answers = json.dumps(answers, ensure_ascii=False)
    result.aptitude_scores = json.dumps(scores, ensure_ascii=False)
    db.session.commit()

    return jsonify({'success': True, 'scores': scores})

# ========== الملف الأكاديمي ==========
@student_bp.route('/profile', methods=['GET'])
@login_required
def profile():
    user_id = session['user_id']
    user = User.query.get(user_id)
    
    subject_grades = {}
    selected_interests = []
    if user.high_school_profile:
        if user.high_school_profile.subject_grades:
            try:
                subject_grades = json.loads(user.high_school_profile.subject_grades)
            except:
                pass
        if user.high_school_profile.interests:
            selected_interests = [i.strip() for i in user.high_school_profile.interests.split('،')]
    
    # جلب نتيجة اختبار الميول إن وُجدت
    assessment_scores = {}
    assessment_completed = False
    assessment_result = AssessmentResult.query.filter_by(user_id=user_id).first()
    if assessment_result and assessment_result.aptitude_scores:
        assessment_scores = assessment_result.get_aptitude_scores()
        assessment_completed = True

    return render_template('hs_profile.html', 
                           user=user, 
                           subject_grades=subject_grades, 
                           selected_interests=selected_interests,
                           assessment_scores=assessment_scores,
                           assessment_completed=assessment_completed)

@student_bp.route('/profile', methods=['POST'])
@login_required
def update_profile():
    user_id = session['user_id']
    user = User.query.get(user_id)
    
    branch = request.form.get('branch', 'علمي')
    overall = request.form.get('overall_percentage', type=float)
    
    math_grade = request.form.get('subject_math', type=float)
    physics_grade = request.form.get('subject_physics', type=float)
    chemistry_grade = request.form.get('subject_chemistry', type=float)
    biology_grade = request.form.get('subject_biology', type=float)
    english_grade = request.form.get('subject_english', type=float)
    
    subject_names = request.form.getlist('subject_name')
    subject_grades = request.form.getlist('subject_grade')
    
    grades_dict = {}
    if math_grade is not None:
        grades_dict['math'] = math_grade
    if physics_grade is not None:
        grades_dict['physics'] = physics_grade
    if chemistry_grade is not None:
        grades_dict['chemistry'] = chemistry_grade
    if biology_grade is not None:
        grades_dict['biology'] = biology_grade
    if english_grade is not None:
        grades_dict['english'] = english_grade
    
    for name, grade in zip(subject_names, subject_grades):
        if name and grade:
            key = name.strip().lower().replace(' ', '_')
            try:
                grades_dict[key] = float(grade)
            except:
                pass
    
    subject_grades_json = json.dumps(grades_dict, ensure_ascii=False)
    
    interests_list = request.form.getlist('interests')
    interests_text = '، '.join(interests_list) if interests_list else ''
    
    if not user.high_school_profile:
        hs_profile = HighSchoolProfile(user_id=user_id)
        db.session.add(hs_profile)
    else:
        hs_profile = user.high_school_profile
    
    hs_profile.branch = branch
    hs_profile.overall_percentage = overall
    hs_profile.subject_grades = subject_grades_json
    hs_profile.interests = interests_text
    
    db.session.commit()
    flash('تم حفظ بيانات الثانوية بنجاح', 'success')
    return redirect(url_for('student.profile'))

# ========== تشغيل المحلل الأكاديمي ==========
@student_bp.route('/analyze')
@login_required
def analyze():
    user_id = session['user_id']
    user = User.query.get(user_id)
    
    if not user.high_school_profile:
        flash('يرجى إدخال بيانات الثانوية أولاً', 'warning')
        return redirect(url_for('student.profile'))
    
    # 1. جلب نتائج اختبار الميول من قاعدة البيانات إن وُجدت
    assessment_result = AssessmentResult.query.filter_by(user_id=user_id).first()
    assessment_scores = {}
    if assessment_result:
        assessment_scores = assessment_result.get_aptitude_scores()
    
    # 2. تحليل بيانات الثانوية مع نتائج الاختبار (تمرير assessment_scores)
    recommendations = AnalysisEngine.analyze_student(user_id, user.high_school_profile, assessment_scores)
    
    if not recommendations:
        flash('لا توجد توصيات مناسبة بناءً على بياناتك الحالية', 'info')
        return redirect(url_for('dashboard.home'))
    
    # حذف التوصيات القديمة
    Recommendation.query.filter_by(user_id=user_id).delete()
    
    # حفظ التوصيات الجديدة مع المسارات المهنية
    for rec in recommendations:
        new_rec = Recommendation(
            user_id=user_id,
            major_title=rec['major_title'],
            match_percentage=rec['match_percentage'],
            reason=rec['reason'],
            career_paths=json.dumps(rec['career_paths'], ensure_ascii=False)
        )
        db.session.add(new_rec)
    db.session.commit()
    
    flash('تم تحليل بياناتك وإنشاء التوصيات بنجاح!', 'success')
    return redirect(url_for('dashboard.home'))