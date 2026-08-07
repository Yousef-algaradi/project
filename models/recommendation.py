from database import db
from datetime import datetime
import json

class Recommendation(db.Model):
    __tablename__ = 'recommendations'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    
    major_title = db.Column(db.String(150))          # اسم التخصص
    match_percentage = db.Column(db.Float)           # نسبة المطابقة 0-100
    reason = db.Column(db.Text)                      # تفسير التوصية
    career_paths = db.Column(db.Text, nullable=True) # ✅ تخزين المسارات المهنية كـ JSON
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    # العلاقة مع المستخدم
    user = db.relationship('User', backref='recommendations', lazy=True)

    def get_career_paths(self):
        """إرجاع قائمة المسارات المهنية من JSON"""
        if self.career_paths:
            return json.loads(self.career_paths)
        return []

    def __repr__(self):
        return f'<Recommendation {self.major_title}>'