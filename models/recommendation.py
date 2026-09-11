# models/recommendation.py
from database import db
from datetime import datetime
import json

class Recommendation(db.Model):
    __tablename__ = 'recommendations'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    
    major_title = db.Column(db.String(150))
    match_percentage = db.Column(db.Float)
    reason = db.Column(db.Text)              # النص المدمج للأسباب (يفصل بـ •)
    weaknesses = db.Column(db.Text, nullable=True)  # ✅ جديد: النص المدمج لنقاط الضعف
    career_paths = db.Column(db.Text, nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    user = db.relationship('User', backref='recommendations', lazy=True)

    def get_career_paths(self):
        """إرجاع قائمة المسارات المهنية من JSON"""
        if self.career_paths:
            try:
                return json.loads(self.career_paths)
            except:
                return []
        return []

    @property
    def career_paths_list(self):
        """خاصية تُستخدم في القوالب لعرض المسارات"""
        return self.get_career_paths()

    @property
    def reasons_list(self):
        """تُرجع قائمة الأسباب من النص المخزن (مفصولة بـ •)"""
        if self.reason:
            parts = [p.strip() for p in self.reason.split('•') if p.strip()]
            return parts if parts else [self.reason]
        return []

    @property
    def weaknesses_list(self):
        """تُرجع قائمة نقاط الضعف من النص المخزن (مفصولة بـ •)"""
        if self.weaknesses:
            parts = [p.strip() for p in self.weaknesses.split('•') if p.strip()]
            return parts if parts else []
        return []

    def __repr__(self):
        return f'<Recommendation {self.major_title}>'