# models/high_school.py
from database import db

class HighSchoolProfile(db.Model):
    __tablename__ = 'high_school_profiles'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), unique=True, nullable=False)
    
    branch = db.Column(db.String(50))                # علمي / أدبي
    overall_percentage = db.Column(db.Float)         # النسبة المئوية (مثلاً 88.5)
    subject_grades = db.Column(db.Text)              # JSON نصي: {"math":95, "physics":88}
    interests = db.Column(db.Text)                   # نص: "برمجة، تصميم، حل مشكلات"

    def __repr__(self):
        return f'<HighSchoolProfile User {self.user_id}>'