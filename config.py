import os
from datetime import timedelta

class Config:
    """Configuration class for Flask application"""

    SECRET_KEY = 'dev-secret-key'

    SQLALCHEMY_DATABASE_URI = 'sqlite:///test.db'

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    SQLALCHEMY_ENGINE_OPTIONS = {
        'pool_recycle': 300,
        'pool_pre_ping': True
    }

    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = ''
    MAIL_PASSWORD = ''
    MAIL_DEFAULT_SENDER = ''

    SCHEDULER_TIMEZONE = 'UTC'

    PERMANENT_SESSION_LIFETIME = timedelta(hours=24)

    APP_URL = 'http://localhost:5000'