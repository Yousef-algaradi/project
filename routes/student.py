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

# بيانات الأقسام - مشتركة بين الأمام والخلف
BRANCH_DATA = {
    'علمي': {
        'subjects': [
            {'key': 'math', 'name': '📐 رياضيات'},
            {'key': 'physics', 'name': '⚡ فيزياء'},
            {'key': 'chemistry', 'name': '🧪 كيمياء'},
            {'key': 'biology', 'name': '🧬 أحياء'},
            {'key': 'english', 'name': '🇬🇧 لغة إنجليزية'}
        ],
        'interests': [
            {'value': 'برمجة', 'icon': '💻'},
            {'value': 'حاسوب', 'icon': '🖥️'},
            {'value': 'شبكات', 'icon': '🌐'},
            {'value': 'أمن سيبراني', 'icon': '🔒'},
            {'value': 'ذكاء اصطناعي', 'icon': '🤖'},
            {'value': 'تطوير ويب', 'icon': '🌍'},
            {'value': 'تحليل بيانات', 'icon': '📊'},
            {'value': 'طب', 'icon': '🏥'},
            {'value': 'هندسة', 'icon': '🏗️'},
            {'value': 'إدارة أعمال', 'icon': '💼'}
        ]
    },
    'أدبي': {
        'subjects': [
            {'key': 'arabic', 'name': '📖 اللغة العربية'},
            {'key': 'history', 'name': '📜 التاريخ'},
            {'key': 'geography', 'name': '🌍 الجغرافيا'},
            {'key': 'islamic', 'name': '☪️ التربية الإسلامية'},
            {'key': 'english', 'name': '🇬🇧 لغة إنجليزية'}
        ],
        'interests': [
            {'value': 'القراءة والكتابة', 'icon': '📚'},
            {'value': 'التحدث والإقناع', 'icon': '🗣️'},
            {'value': 'الإعلام والصحافة', 'icon': '📰'},
            {'value': 'القانون والعدالة', 'icon': '⚖️'},
            {'value': 'التاريخ والحضارات', 'icon': '🏛️'},
            {'value': 'اللغات الأجنبية', 'icon': '🌐'},
            {'value': 'التعليم والتدريس', 'icon': '👨‍🏫'},
            {'value': 'إدارة الأعمال', 'icon': '💼'},
            {'value': 'الفنون والتصميم', 'icon': '🎨'},
            {'value': 'العمل الاجتماعي', 'icon': '🤝'}
        ]
    }
}


# ========== عرض صفحة اختبار الميول ==========
@student_bp.route('/assessment')
@login_required
def assessment():
    user_id = session['user_id']
    user = User.query.get(user_id)
    
    branch = 'علمي'
    if user.high_school_profile and user.high_school_profile.branch:
        branch = user.high_school_profile.branch
    
    aptitude_questions = AssessmentEngine.APTITUDE_QUESTIONS
    subject_questions = AssessmentEngine.SUBJECT_QUESTIONS.get(branch, {})
    
    return render_template('assessment.html', 
                           aptitude_questions=aptitude_questions,
                           subject_questions=subject_questions,
                           branch=branch)


# ========== استقبال نتائج اختبار الميول والمواد ==========
@student_bp.route('/assessment/submit', methods=['POST'])
@login_required
def submit_assessment():
    user_id = session['user_id']
    user = User.query.get(user_id)
    data = request.get_json()
    if not data:
        return jsonify({'error': 'لا توجد بيانات'}), 400

    aptitude_answers = data.get('aptitude_answers', {})
    aptitude_scores = AssessmentEngine.calculate_dimension_scores(aptitude_answers)

    subject_answers = data.get('subject_answers', {})
    branch = 'علمي'
    if user.high_school_profile and user.high_school_profile.branch:
        branch = user.high_school_profile.branch
    subject_scores = AssessmentEngine.calculate_subject_scores(subject_answers, branch)

    result = AssessmentResult.query.filter_by(user_id=user_id).first()
    if not result:
        result = AssessmentResult(user_id=user_id)
        db.session.add(result)

    result.aptitude_answers = json.dumps(aptitude_answers, ensure_ascii=False)
    result.aptitude_scores = json.dumps(aptitude_scores, ensure_ascii=False)
    result.subject_answers = json.dumps(subject_answers, ensure_ascii=False)
    result.subject_scores = json.dumps(subject_scores, ensure_ascii=False)
    db.session.commit()

    return jsonify({
        'success': True,
        'aptitude_scores': aptitude_scores,
        'subject_scores': subject_scores
    })


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
    
    assessment_scores = {}
    subject_test_scores = {}
    assessment_completed = False
    assessment_result = AssessmentResult.query.filter_by(user_id=user_id).first()
    if assessment_result:
        if assessment_result.aptitude_scores:
            assessment_scores = assessment_result.get_aptitude_scores()
            assessment_completed = True
        if assessment_result.subject_scores:
            subject_test_scores = assessment_result.get_subject_scores()

    return render_template('hs_profile.html', 
                           user=user, 
                           subject_grades=subject_grades, 
                           selected_interests=selected_interests,
                           assessment_scores=assessment_scores,
                           subject_test_scores=subject_test_scores,
                           assessment_completed=assessment_completed,
                           branch_data=BRANCH_DATA)


@student_bp.route('/profile', methods=['POST'])
@login_required
def update_profile():
    user_id = session['user_id']
    user = User.query.get(user_id)
    
    branch = request.form.get('branch', 'علمي')
    overall = request.form.get('overall_percentage', type=float)
    
    grades_dict = {}
    if branch in BRANCH_DATA:
        for sub in BRANCH_DATA[branch]['subjects']:
            key = sub['key']
            value = request.form.get('subject_' + key, type=float)
            if value is not None:
                grades_dict[key] = value
    
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
    
    # قراءة الإجراء التالي
    next_action = request.form.get('next_action', 'analyze')
    
    if next_action == 'assessment':
        return redirect(url_for('student.assessment'))
    else:
        return redirect(url_for('student.analyze'))


# ========== تشغيل المحلل الأكاديمي ==========
@student_bp.route('/analyze')
@login_required
def analyze():
    user_id = session['user_id']
    user = User.query.get(user_id)
    
    if not user.high_school_profile:
        flash('يرجى إدخال بيانات الثانوية أولاً', 'warning')
        return redirect(url_for('student.profile'))
    
    assessment_result = AssessmentResult.query.filter_by(user_id=user_id).first()
    assessment_scores = {}
    subject_test_scores = {}
    if assessment_result:
        assessment_scores = assessment_result.get_aptitude_scores()
        subject_test_scores = assessment_result.get_subject_scores()
    
    recommendations = AnalysisEngine.analyze_student(
        user_id, 
        user.high_school_profile, 
        assessment_scores,
        subject_test_scores
    )
    
    if not recommendations:
        flash('لا توجد توصيات مناسبة بناءً على بياناتك الحالية', 'info')
        return redirect(url_for('dashboard.home'))
    
    Recommendation.query.filter_by(user_id=user_id).delete()
    
    for rec in recommendations:
        new_rec = Recommendation(
    user_id=user_id,
    major_title=rec['major_title'],
    match_percentage=rec['match_percentage'],
    reason=' • '.join(rec['reasons_list']),
    weaknesses=' • '.join(rec.get('weaknesses_list', [])),  # ✅ جديد
    career_paths=json.dumps(rec['career_paths'], ensure_ascii=False)
)
        
        db.session.add(new_rec)
    db.session.commit()
    
    flash('تم تحليل بياناتك وإنشاء التوصيات بنجاح!', 'success')
    return redirect(url_for('dashboard.home', tab='recommendations'))
# ========== البدء من جديد (حذف كل شيء) ==========
@student_bp.route('/reset-all')
@login_required
def reset_all():
    user_id = session['user_id']
    user = User.query.get(user_id)
    
    # حذف بيانات الثانوية
    if user.high_school_profile:
        db.session.delete(user.high_school_profile)
    
    # حذف نتائج الاختبار
    assessment_result = AssessmentResult.query.filter_by(user_id=user_id).first()
    if assessment_result:
        db.session.delete(assessment_result)
    
    # حذف التوصيات
    Recommendation.query.filter_by(user_id=user_id).delete()
    
    db.session.commit()
    flash('تم حذف جميع بياناتك بنجاح. يمكنك البدء من جديد.', 'success')
    return redirect(url_for('student.profile'))