# models/university.py
from database import db
from datetime import datetime
import json


class UniversityProfile(db.Model):
    """بيانات الطالب الجامعي (مكملة لبيانات الثانوية)"""
    __tablename__ = 'university_profiles'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), unique=True, nullable=False)

    major = db.Column(db.String(150))                    # التخصص (من قائمة مخزنة)
    preferred_track = db.Column(db.String(100))          # المسار المفضل (ai/cyber/data_science)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    user = db.relationship('User', backref='university_profile', uselist=False)

    def __repr__(self):
        return f'<UniversityProfile {self.major}>'


class CareerPath(db.Model):
    """المسار المهني (مثلاً: محلل بيانات)"""
    __tablename__ = 'career_paths'

    id = db.Column(db.Integer, primary_key=True)
    major_key = db.Column(db.String(50), nullable=False, index=True)  # 'ai', 'cyber', 'data_science'
    slug = db.Column(db.String(100), nullable=False, unique=True)     # 'data-analyst'
    title = db.Column(db.String(200), nullable=False)                 # اسم المسار
    description = db.Column(db.Text)                                   # وصف قصير
    icon = db.Column(db.String(50))                                    # emoji
    difficulty = db.Column(db.String(50))                              # مبتدئ/متوسط/متقدم
    estimated_hours = db.Column(db.Integer)                            # الساعات المتوقعة
    total_stages = db.Column(db.Integer, default=0)                    # عدد المراحل
    order_index = db.Column(db.Integer, default=0)                     # ترتيب العرض
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    stages = db.relationship(
        'CareerStage',
        backref='career_path',
        lazy=True,
        cascade='all, delete-orphan',
        order_by='CareerStage.stage_number'
    )

    def __repr__(self):
        return f'<CareerPath {self.slug}>'


class CareerStage(db.Model):
    """مرحلة داخل المسار المهني (مثلاً: تعلم SQL)"""
    __tablename__ = 'career_stages'

    id = db.Column(db.Integer, primary_key=True)
    career_path_id = db.Column(db.Integer, db.ForeignKey('career_paths.id'), nullable=False)
    stage_number = db.Column(db.Integer, nullable=False)             # 1, 2, 3...
    title = db.Column(db.String(200), nullable=False)                # اسم المرحلة
    description = db.Column(db.Text)                                  # وصف المرحلة
    objectives = db.Column(db.Text)                                   # JSON: ["...", "..."]
    practical_task = db.Column(db.Text)                               # التطبيق العملي
    youtube_ar = db.Column(db.String(500))                            # رابط يوتيوب عربي
    youtube_en = db.Column(db.String(500))                            # رابط يوتيوب إنجليزي
    passing_score = db.Column(db.Integer, default=11)                 # 11 من 15 = 73%
    total_quiz_questions = db.Column(db.Integer, default=10)          # عدد الأسئلة المعروضة

    questions = db.relationship(
        'QuizQuestion',
        backref='stage',
        lazy=True,
        cascade='all, delete-orphan'
    )

    def get_objectives(self):
        """إرجاع الأهداف كقائمة"""
        if self.objectives:
            try:
                return json.loads(self.objectives)
            except:
                return []
        return []

    def __repr__(self):
        return f'<CareerStage {self.stage_number}: {self.title}>'


class QuizQuestion(db.Model):
    """سؤال في بنك أسئلة المرحلة"""
    __tablename__ = 'quiz_questions'

    id = db.Column(db.Integer, primary_key=True)
    stage_id = db.Column(db.Integer, db.ForeignKey('career_stages.id'), nullable=False)
    question_text = db.Column(db.Text, nullable=False)
    options = db.Column(db.Text, nullable=False)              # JSON: {"A": "...", "B": "...", "C": "...", "D": "..."}
    correct_answer = db.Column(db.String(2), nullable=False)  # 'A', 'B', 'C', 'D'
    difficulty = db.Column(db.String(20), default='easy')      # easy / medium / hard

    def get_options(self):
        """إرجاع الخيارات كقاموس"""
        if self.options:
            try:
                return json.loads(self.options)
            except:
                return {}
        return {}

    def __repr__(self):
        return f'<QuizQuestion {self.id}>'


class CareerProgress(db.Model):
    """تقدم المستخدم في المسار المهني"""
    __tablename__ = 'career_progress'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False, index=True)
    career_path_id = db.Column(db.Integer, db.ForeignKey('career_paths.id'), nullable=False, index=True)

    current_stage = db.Column(db.Integer, default=1)          # المرحلة الحالية
    completed_stages = db.Column(db.Text, default='[]')        # JSON: [1, 2, 3]
    total_xp = db.Column(db.Integer, default=0)                # إجمالي النقاط
    attempts = db.Column(db.Text, default='{}')                # JSON: {"1": [{"score": 8, "date": "..."}, ...]}
    last_activity = db.Column(db.DateTime, default=datetime.utcnow)
    streak_days = db.Column(db.Integer, default=0)             # أيام متتالية
    last_streak_date = db.Column(db.Date)                       # آخر يوم للنشاط
    is_completed = db.Column(db.Boolean, default=False)        # اكتمل المسار
    completed_at = db.Column(db.DateTime)                       # تاريخ الإكمال

    user = db.relationship('User', backref='career_progress_entries')
    career_path = db.relationship('CareerPath', backref='progress_entries')

    __table_args__ = (
        db.UniqueConstraint('user_id', 'career_path_id', name='unique_user_career'),
    )

    def get_completed_stages(self):
        """إرجاع قائمة المراحل المكتملة"""
        if self.completed_stages:
            try:
                return json.loads(self.completed_stages)
            except:
                return []
        return []

    def get_attempts(self):
        """إرجاع كل محاولات الاختبارات"""
        if self.attempts:
            try:
                return json.loads(self.attempts)
            except:
                return {}
        return {}

    def get_progress_percentage(self):
        """نسبة التقدم في المسار"""
        if not self.career_path or not self.career_path.total_stages:
            return 0
        completed = len(self.get_completed_stages())
        return round((completed / self.career_path.total_stages) * 100, 1)

    def __repr__(self):
        return f'<CareerProgress User {self.user_id} - Path {self.career_path_id}>'