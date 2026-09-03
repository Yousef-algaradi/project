# models/user.py
from database import db
import json
from datetime import datetime

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password_hash = db.Column(db.String(256), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    # العلاقة (one-to-one) مع ملف الثانوية
    high_school_profile = db.relationship('HighSchoolProfile', backref='user', uselist=False, lazy=True)

    def __repr__(self):
        return f'<User {self.email}>'

    

class AssessmentResult(db.Model):
    __tablename__ = 'assessment_results'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), unique=True, nullable=False)
    aptitude_answers = db.Column(db.Text, default='{}')   # JSON: {question_id: option_id}
    aptitude_scores = db.Column(db.Text, default='{}')    # JSON: {dimension: score}
    completed_at = db.Column(db.DateTime, default=datetime.utcnow)

    user = db.relationship('User', backref='assessment_result', uselist=False)

    def get_aptitude_scores(self):
        if self.aptitude_scores:
            return json.loads(self.aptitude_scores)
        return {}

    def __repr__(self):
        return f'<AssessmentResult User {self.user_id}>'