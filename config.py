# config.py
import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'my-super-secret-key-2026'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///highschool.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False