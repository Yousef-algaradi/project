# routes/main.py
from flask import Blueprint, render_template, session, redirect, url_for, flash
from utils.decorators import login_required
from models.user import User
from database import db

main_bp = Blueprint('main', __name__)


# ==========================================
# الصفحة الرئيسية
# ==========================================
@main_bp.route('/')
def index():
    return render_template('index.html')


# ==========================================
# شاشة اختيار نوع المستخدم
# ==========================================
@main_bp.route('/welcome-choice')
@login_required
def welcome_choice():
    user_id = session['user_id']
    user = User.query.get(user_id)
    
    # ✅ التوجيه الذكي حسب user_type
    if user.user_type == 'university':
        return redirect(url_for('university.dashboard'))
    elif user.user_type == 'high_school':
        return redirect(url_for('dashboard.home'))
    
    # مستخدم جديد → اعرض الشاشة
    return render_template('welcome_choice.html', user=user)


# ==========================================
# حفظ اختيار نوع المستخدم
# ==========================================
@main_bp.route('/set-user-type/<user_type>')
@login_required
def set_user_type(user_type):
    if user_type not in ['high_school', 'university']:
        flash('نوع المستخدم غير صحيح', 'danger')
        return redirect(url_for('main.welcome_choice'))
    
    user_id = session['user_id']
    user = User.query.get(user_id)
    
    user.user_type = user_type
    db.session.commit()
    
    if user_type == 'university':
        flash('🎓 تم تفعيل مسار الطالب الجامعي', 'success')
        return redirect(url_for('university.setup'))
    else:
        flash('📚 تم تفعيل مسار الطالب الثانوي', 'success')
        return redirect(url_for('student.profile'))


# ==========================================
# تبديل نوع المستخدم
# ==========================================
@main_bp.route('/switch-to/<target_type>')
@login_required
def switch_to(target_type):
    if target_type not in ['high_school', 'university']:
        flash('نوع المستخدم غير صحيح', 'danger')
        return redirect(url_for('main.index'))
    
    user_id = session['user_id']
    user = User.query.get(user_id)
    
    user.user_type = target_type
    db.session.commit()
    
    if target_type == 'university':
        # إذا كان لديه ملف جامعي، وجّهه للداش مباشرة
        from models.university import UniversityProfile
        uni_profile = UniversityProfile.query.filter_by(user_id=user_id).first()
        
        if uni_profile and uni_profile.preferred_track:
            flash('🎓 تم التبديل لمسار الجامعة', 'success')
            return redirect(url_for('university.dashboard'))
        else:
            flash('🎓 اختر تخصصك ومسارك', 'info')
            return redirect(url_for('university.setup'))
    else:
        flash('📚 تم التبديل لمسار الثانوية', 'success')
        return redirect(url_for('dashboard.home'))