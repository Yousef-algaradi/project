# routes/student.py
from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from utils.decorators import login_required
from models.user import User
from models.high_school import HighSchoolProfile
from models.recommendation import Recommendation
from services.analysis_engine import AnalysisEngine

from database import db
import json

student_bp = Blueprint('student', __name__)

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
    
    return render_template('hs_profile.html', user=user, subject_grades=subject_grades, selected_interests=selected_interests)

@student_bp.route('/profile', methods=['POST'])
@login_required
def update_profile():
    user_id = session['user_id']
    user = User.query.get(user_id)
    
    branch = request.form.get('branch', 'علمي')
    overall = request.form.get('overall_percentage', type=float)
    
    # جلب درجات المواد الخمسة
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

@student_bp.route('/analyze')
@login_required
def analyze():
    user_id = session['user_id']
    user = User.query.get(user_id)
    
    if not user.high_school_profile:
        flash('يرجى إدخال بيانات الثانوية أولاً', 'warning')
        return redirect(url_for('student.profile'))
    
    # 1. تحليل بيانات الثانوية
    recommendations = AnalysisEngine.analyze_student(user_id, user.high_school_profile)
    
    # 2. دمج نتائج الاختبار (نفس الكود)
    assessment_scores = session.get('assessment_scores', {})
    if assessment_scores and recommendations:
        mapping = {
            'data science': 'data_science',
            'ai': 'ai',
            'cyber security': 'cyber',
            'it': 'it',
            'software engineering': 'software'
        }
        for rec in recommendations:
            major_key = rec['major_title'].split('(')[-1].strip().replace(')', '').lower()
            mapped_key = mapping.get(major_key, major_key)
            if mapped_key in assessment_scores:
                assessment_score = assessment_scores[mapped_key]
                rec['match_percentage'] = round((rec['match_percentage'] * 0.7) + (assessment_score * 0.3), 2)
    
    if not recommendations:
        flash('لا توجد توصيات مناسبة بناءً على بياناتك الحالية', 'info')
        return redirect(url_for('dashboard.home'))
    
    # ✅ حذف التوصيات القديمة
    Recommendation.query.filter_by(user_id=user_id).delete()
    
    # ✅ حفظ التوصيات الجديدة مع المسارات المهنية
    for rec in recommendations:
        new_rec = Recommendation(
            user_id=user_id,
            major_title=rec['major_title'],
            match_percentage=rec['match_percentage'],
            reason=rec['reason'],
            career_paths=json.dumps(rec['career_paths'], ensure_ascii=False)  # ← التغيير الرئيسي
        )
        db.session.add(new_rec)
    db.session.commit()
    
    # ❌ حذف السطر التالي (لم يعد ضرورياً)
    # session['career_paths'] = {rec['major_title']: rec['career_paths'] for rec in recommendations}
    
    flash('تم تحليل بياناتك وإنشاء التوصيات بنجاح!', 'success')
    return redirect(url_for('dashboard.home'))