import os
from dotenv.main import load_dotenv

load_dotenv('.env')

class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SESSION_COOKIE_SECURE = True
    SESSION_COOKIE_HTTPONLY = True
    SESSION_COOKIE_SAMESITE = 'None'
    MONGODB_SETTINGS = {
        'db': os.getenv('DATABASE_NAME'),
        'host': os.getenv('DATABASE_URL'),
    }

class ProductionConfig(Config):
    DEBUG = False
    SECRET_KEY = os.getenv('SECRET_KEY')


class DevelopmentConfig(Config):
    ENV = 'development'
    DEVELOPMENT = True
    SECRET_KEY = os.getenv('SECRET_KEY')
    OAUTHLIB_INSECURE_TRANSPORT = True


class TestingConfig(Config):
    TESTING = True