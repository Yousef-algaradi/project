# services/auth_service.py
from werkzeug.security import generate_password_hash, check_password_hash
from models.user import User
from database import db

class AuthService:

    @staticmethod
    def hash_password(password):
        return generate_password_hash(password)

    @staticmethod
    def verify_password(hashed, password):
        return check_password_hash(hashed, password)

    @staticmethod
    def register_user(name, email, password):
        # التحقق من عدم وجود البريد مسبقاً
        if User.query.filter_by(email=email).first():
            return None, 'البريد الإلكتروني مسجل بالفعل'
        
        hashed = AuthService.hash_password(password)
        new_user = User(name=name, email=email, password_hash=hashed)
        db.session.add(new_user)
        db.session.commit()
        return new_user, None

    @staticmethod
    def login_user(email, password):
        user = User.query.filter_by(email=email).first()
        if not user:
            return None, 'البريد الإلكتروني غير موجود'
        if not AuthService.verify_password(user.password_hash, password):
            return None, 'كلمة المرور غير صحيحة'
        return user, None