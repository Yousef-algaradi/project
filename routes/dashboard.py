# routes/dashboard.py
from flask import Blueprint, render_template, session, redirect, url_for, flash
from utils.decorators import login_required
from models.user import User
from models.recommendation import Recommendation
import json

dashboard_bp = Blueprint('dashboard', __name__)


@dashboard_bp.route('/')
@login_required
def home():
    user_id = session['user_id']
    user = User.query.get(user_id)
    
    # ✅ إذا كان الطالب "جامعي" → وجّهه لداش الجامعة
    if user.user_type == 'university':
        return redirect(url_for('university.dashboard'))
    
    # جلب التوصيات مرتبة تنازلياً حسب نسبة التوافق
    recommendations = Recommendation.query.filter_by(user_id=user_id).order_by(
        Recommendation.match_percentage.desc()
    ).all()
    
    return render_template('dashboard.html', user=user, recommendations=recommendations)