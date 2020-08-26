import os
# All configuration store here
class CeleryConfig(object):
    CELERY_BROKER_URL = os.environ.get("CELERY_BROKER_URL") or "redis://localhost:6379/0"
    CELERY_RESULT_BACKEND = os.environ.get("CELERY_BACKEND_URL") or "redis://localhost:6379/0" #The CELERY_RESULT_BACKEND option is to have Celery store status and results from tasks

class Config(object):
    """The common configurations for all environments"""
    SESSION_COOKIE_SECURE=False
    SESSION_COOKIE_HTTPONLY=True
    SESSION_COOKIE_SAMESITE='Lax'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.environ.get("SECRET_KEY") or "ks;a;bf88jlk;67890"
    
    
class DevelopmentConfig(Config):
    # all config: https://flask.palletsprojects.com/en/1.1.x/config/
    ENV = 'development' #production
    DEBUG = True
    TESTING = True
    # Database & SQLAlchemy configs
    SQLALCHEMY_DATABASE_URI = os.environ.get("SQLALCHEMY_DATABASE_URI")
    # SQLALCHEMY_BINDS = {
    #     'REPORTER':      'oracle+cx_oracle://TEST:123456@127.0.0.1:1521/DB81',
    #     'SQLITE':        'sqlite://', #in memory sqlite db
    # }
    # WTF_CSRF_ENABLED = False #only in TEST env -> do NOT do it on any other env
    
class ProductionConfig(Config):
    # all config: https://flask.palletsprojects.com/en/1.1.x/config/
    ENV = 'production' #production
    DEBUG = False
    TESTING = False
    # Database & SQLAlchemy configs
    SQLALCHEMY_DATABASE_URI = os.environ.get("SQLALCHEMY_DATABASE_URI")
    
class TestConfig(Config):
    ENV = 'test'
    DEBUG = True
    TESTING = True
    # Database & SQLAlchemy configs -> Pytest ALWAYS isolate databases for EACH test. -> always clear database after test.
    SQLALCHEMY_DATABASE_URI = "sqlite:///app2.db"
    WTF_CSRF_ENABLED = False #only in TEST env -> do NOT do it on any other env