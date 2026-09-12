# config.py
import os
import secrets
import warnings
from datetime import timedelta


class Config:
    # ==========================================
    # SECRET_KEY — إجباري في الإنتاج
    # ==========================================
    SECRET_KEY = os.environ.get('SECRET_KEY')
    if not SECRET_KEY:
        SECRET_KEY = secrets.token_hex(32)
        warnings.warn(
            "⚠️ SECRET_KEY غير مضبوط في متغيرات البيئة! "
            "يُستخدم مفتاح عشوائي — الجلسات ستُبطَل عند إعادة التشغيل.",
            RuntimeWarning,
            stacklevel=2
        )

    # ==========================================
    # قاعدة البيانات
    # ==========================================
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', 'sqlite:///highschool.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ENGINE_OPTIONS = {
        'pool_pre_ping': True,
    }

    # ==========================================
    # حماية الجلسات
    # ==========================================
    SESSION_COOKIE_HTTPONLY = True
    SESSION_COOKIE_SAMESITE = 'Lax'
    SESSION_COOKIE_SECURE = os.environ.get('FLASK_ENV') == 'production'
    PERMANENT_SESSION_LIFETIME = timedelta(days=7)

    # ==========================================
    # حدود الطلبات
    # ==========================================
    MAX_CONTENT_LENGTH = 1 * 1024 * 1024  # 1MB

    # ==========================================
    # وضع التشغيل
    # ==========================================
    DEBUG = os.environ.get('FLASK_DEBUG', 'False').lower() == 'true'