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
    SECRET_KEY = "34567890-cvnbm,./tyijlk;67890vbnm,;ltyuilk.,dev"
    # Database & SQLAlchemy configs
    SQLALCHEMY_DATABASE_URI = "mysql+mysqldb://test:123456@localhost/test"
    SQLALCHEMY_BINDS = {
        'REPORTER':      'oracle+cx_oracle://PARTNERCTH:epay123123@172.16.10.81:1521/DB81',
        'SQLITE':        'sqlite://', #in memory sqlite db
    }
    
class ProductionConfig(Config):
    # all config: https://flask.palletsprojects.com/en/1.1.x/config/
    ENV = 'production' #production
    DEBUG = False
    TESTING = False
    SECRET_KEY = "34567890-cvnbm?./tyijlk;67890vbnm,;ltyuilk.,prodd"
    # Database & SQLAlchemy configs
    SQLALCHEMY_DATABASE_URI = "mysql+mysqldb://reportapi:NiDIFaXeDoCe7Ova7I3A4I33macOn6@172.16.213.18/test"
    SQLALCHEMY_BINDS = {
        'REPORTER':      'oracle+cx_oracle://REPORTER:REPORTER123@DG1',
        'SQLITE':        'sqlite://', #in memory sqlite db
    }
    
class TestConfig(Config):
    ENV = 'test'
    DEBUG = True
    TESTING = True
    SECRET_KEY = "34567890-cvnbm,./tyijlk;67890vbnm,;ltyuilk.,test"
    # Database & SQLAlchemy configs
    SQLALCHEMY_DATABASE_URI = "sqlite://"