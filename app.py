# app.py
from flask import Flask
from config import Config
from database import init_db

from routes.main import main_bp
from routes.auth import auth_bp
from routes.student import student_bp
from routes.dashboard import dashboard_bp
from models.university import UniversityProfile, CareerPath, CareerStage, QuizQuestion, CareerProgress
from routes.university import university_bp
app = Flask(__name__)
app.config.from_object(Config)

init_db(app)

app.register_blueprint(main_bp)
app.register_blueprint(auth_bp, url_prefix='/auth')
app.register_blueprint(student_bp, url_prefix='/student')
app.register_blueprint(dashboard_bp, url_prefix='/dashboard')
app.register_blueprint(university_bp, url_prefix='/university')

if __name__ == '__main__':
    app.run(debug=True)