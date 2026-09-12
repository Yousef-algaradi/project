# app.py
import os
from flask import Flask
from config import Config


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # ==========================================
    # 1. استيراد كل النماذج (لتسجيلها في metadata)
    # ==========================================
    from models import user, high_school, recommendation, university  # noqa

    # ==========================================
    # 2. تهيئة قاعدة البيانات
    # ==========================================
    from database import init_db
    init_db(app)

    # ==========================================
    # 3. تسجيل Blueprints
    # ==========================================
    from routes.main import main_bp
    from routes.auth import auth_bp
    from routes.student import student_bp
    from routes.dashboard import dashboard_bp
    from routes.university import university_bp

    app.register_blueprint(main_bp)
    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(student_bp, url_prefix='/student')
    app.register_blueprint(dashboard_bp, url_prefix='/dashboard')
    app.register_blueprint(university_bp, url_prefix='/university')

    return app


if __name__ == '__main__':
    app = create_app()
    app.run(
        debug=app.config['DEBUG'],
        host='127.0.0.1',
        port=5000
    )