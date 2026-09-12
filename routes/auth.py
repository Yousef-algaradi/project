# routes/auth.py
from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from services.auth_service import AuthService

auth_bp = Blueprint('auth', __name__)


# ==========================================
# عرض صفحة التسجيل
# ==========================================
@auth_bp.route('/register', methods=['GET'])
def register_page():
    return render_template('register.html')


# ==========================================
# معالجة التسجيل
# ==========================================
@auth_bp.route('/register', methods=['POST'])
def register():
    name = request.form.get('name', '').strip()
    email = request.form.get('email', '').strip()
    password = request.form.get('password', '')

    # ✅ لو ناقص → render_template مع القيم
    if not name or not email or not password:
        flash('جميع الحقول مطلوبة', 'danger')
        return render_template('register.html',
                               name=name,
                               email=email)

    user, error = AuthService.register_user(name, email, password)
    if error:
        flash(error, 'danger')
        # ✅ نرجع نفس الصفحة مع القيم
        return render_template('register.html',
                               name=name,
                               email=email)

    # ==========================================
    # ✅ الحل: بعد التسجيل الناجح → صفحة الدخول
    # ==========================================
    flash(f'مرحباً {name}، تم إنشاء حسابك بنجاح. سجّل دخولك الآن.', 'success')
    return redirect(url_for('auth.login_page'))


# ==========================================
# عرض صفحة تسجيل الدخول
# ==========================================
@auth_bp.route('/login', methods=['GET'])
def login_page():
    return render_template('login.html')


# ==========================================
# معالجة تسجيل الدخول
# ==========================================
@auth_bp.route('/login', methods=['POST'])
def login():
    email = request.form.get('email', '').strip()
    password = request.form.get('password', '')

    user, error = AuthService.login_user(email, password)
    if error:
        flash(error, 'danger')
        # ✅ نحفظ الإيميل، كلمة السر تفرغ
        return render_template('login.html',
                               email=email)

    # ✅ ضد Session Fixation
    session.clear()
    session.permanent = True
    session['user_id'] = user.id
    session['user_name'] = user.name

    flash(f'مرحباً {user.name}، تم تسجيل الدخول بنجاح', 'success')

    if user.user_type == 'university':
        return redirect(url_for('university.dashboard'))
    elif user.user_type == 'high_school':
        return redirect(url_for('dashboard.home'))
    else:
        return redirect(url_for('main.welcome_choice'))


# ==========================================
# تسجيل الخروج (POST — آمن من CSRF)
# ==========================================
@auth_bp.route('/logout', methods=['POST'])
def logout():
    session.clear()
    flash('تم تسجيل الخروج', 'info')
    return redirect(url_for('main.index'))