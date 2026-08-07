from flask import Blueprint, render_template, session, redirect, url_for, flash
from utils.decorators import login_required
from models.user import User
from models.recommendation import Recommendation
import json  # ✅ إضافة import لتحويل JSON

dashboard_bp = Blueprint('dashboard', __name__)

@dashboard_bp.route('/')
@login_required
def home():
    user_id = session['user_id']
    user = User.query.get(user_id)
    
    # جلب جميع التوصيات مرتبة من الأحدث
    recommendations = Recommendation.query.filter_by(user_id=user_id).order_by(Recommendation.match_percentage.desc()).all()
    
    # ✅ تحويل career_paths من JSON إلى قائمة لكل توصية
    for rec in recommendations:
        rec.career_paths_list = rec.get_career_paths()  # استخدام الدالة المساعدة من الموديل
    
    return render_template('dashboard.html', user=user, recommendations=recommendations)