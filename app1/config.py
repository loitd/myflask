import os
# All configuration store here
class Config(object):
    """The common configurations for all environments"""
    SESSION_COOKIE_SECURE=False
    SESSION_COOKIE_HTTPONLY=True
    SESSION_COOKIE_SAMESITE='Lax'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
class DevelopmentConfig(Config):
    # all config: https://flask.palletsprojects.com/en/1.1.x/config/
    ENV = 'development' #production
    DEBUG = True
    TESTING = True
    SECRET_KEY = os.environ.get("SECRET_KEY") or "ks;a;bf88jlk;67890"
    # Database & SQLAlchemy configs
    SQLALCHEMY_DATABASE_URI = os.environ.get("SQLALCHEMY_DATABASE_URI")
    # SQLALCHEMY_BINDS = {
    #     'REPORTER':      'oracle+cx_oracle://TEST:123456@127.0.0.1:1521/DB81',
    #     'SQLITE':        'sqlite://', #in memory sqlite db
    # }
    
class ProductionConfig(Config):
    # all config: https://flask.palletsprojects.com/en/1.1.x/config/
    ENV = 'production' #production
    DEBUG = False
    TESTING = False
    SECRET_KEY = os.environ.get("SECRET_KEY")
    # Database & SQLAlchemy configs
    SQLALCHEMY_DATABASE_URI = os.environ.get("SQLALCHEMY_DATABASE_URI")
    
class TestConfig(Config):
    ENV = 'test'
    DEBUG = True
    TESTING = True
    SECRET_KEY = os.environ.get("SECRET_KEY") or "0-cm,./tlk;6"
    # Database & SQLAlchemy configs
    SQLALCHEMY_DATABASE_URI = "sqlite://"