# services/auth_service.py
import re
from werkzeug.security import generate_password_hash, check_password_hash
from models.user import User
from database import db


class AuthService:

    # ==========================================
    # ثوابت
    # ==========================================
    MIN_PASSWORD_LENGTH = 6
    EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')

    # ==========================================
    # تشفير / تحقق
    # ==========================================
    @staticmethod
    def hash_password(password):
        return generate_password_hash(password, method='pbkdf2:sha256:600000')

    @staticmethod
    def verify_password(hashed, password):
        if not hashed:
            return False
        return check_password_hash(hashed, password)

    # ==========================================
    # تحقق من المدخلات
    # ==========================================
    @staticmethod
    def validate_email(email):
        if not email or not AuthService.EMAIL_REGEX.match(email):
            return False, 'صيغة البريد الإلكتروني غير صحيحة'
        return True, None

    @staticmethod
    def validate_password(password):
        if not password:
            return False, 'كلمة المرور مطلوبة'
        if len(password) < AuthService.MIN_PASSWORD_LENGTH:
            return False, f'كلمة المرور يجب أن تكون {AuthService.MIN_PASSWORD_LENGTH} أحرف على الأقل'
        if not any(c.isdigit() for c in password):
            return False, 'كلمة المرور يجب أن تحتوي على رقم واحد على الأقل'
        if not any(c.isalpha() for c in password):
            return False, 'كلمة المرور يجب أن تحتوي على حرف واحد على الأقل'
        return True, None

    # ==========================================
    # تسجيل مستخدم جديد
    # ==========================================
    @staticmethod
    def register_user(name, email, password):
        # تحقق من المدخلات
        if not name or len(name.strip()) < 2:
            return None, 'الاسم مطلوب (حرفين على الأقل)'

        valid, err = AuthService.validate_email(email)
        if not valid:
            return None, err

        valid, err = AuthService.validate_password(password)
        if not valid:
            return None, err

        # فحص التكرار
        if User.query.filter_by(email=email.lower().strip()).first():
            return None, 'البريد الإلكتروني مسجل بالفعل'

        # إنشاء المستخدم
        new_user = User(
            name=name.strip(),
            email=email.lower().strip(),
            password_hash=AuthService.hash_password(password)
        )
        db.session.add(new_user)
        db.session.commit()
        return new_user, None

    # ==========================================
    # تسجيل الدخول
    # ==========================================
    @staticmethod
    def login_user(email, password):
        if not email or not password:
            return None, 'البريد وكلمة المرور مطلوبان'

        user = User.query.filter_by(email=email.lower().strip()).first()

        # ⚠️ رسالة موحّدة (لا نكشف إن كان الإيميل موجوداً)
        if not user or not AuthService.verify_password(user.password_hash, password):
            return None, 'البريد الإلكتروني أو كلمة المرور غير صحيحة'

        return user, None