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
    
    # جلب جميع التوصيات مرتبة من الأحدث
    recommendations = Recommendation.query.filter_by(user_id=user_id).order_by(Recommendation.match_percentage.desc()).all()
    
    # لا حاجة لتحويل career_paths هنا - الخاصية career_paths_list جاهزة من الموديل
    
    return render_template('dashboard.html', user=user, recommendations=recommendations)