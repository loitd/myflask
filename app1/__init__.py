# Moving all app1 general to here
# Instead of placing at Views

from flask import Flask, current_app
from lutils.utils import printlog, printwait
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
import os
from flask_principal import Principal, Permission, RoleNeed

_static = os.path.join(os.path.dirname(__file__), 'static')
_templates = os.path.join(os.path.dirname(__file__), 'templates')

db = SQLAlchemy()
mig = Migrate()
loginmgr = LoginManager()
prcp = Principal()

def create_app(theConfig=None):
    _app = Flask(__name__, static_folder = _static, template_folder=_templates)
    
    # Check both this env exists and equals to
    if os.environ.get("FLASK_ENV") and os.environ.get("FLASK_ENV").upper() == "PRODUCTION":
        _app.config.from_object('app1.config.ProductionConfig')
    elif os.environ.get("FLASK_ENV") and os.environ.get("FLASK_ENV").upper() == "DEVELOPMENT":
        _app.config.from_object('app1.config.DevelopmentConfig')
    else:
        _app.config.from_object('app1.config.TestConfig')
    
    # Update the configuration
    if theConfig is not None:
        _app.config.update(theConfig)

    # Init the database for app here
    # _db = SQLAlchemy(_app)
    db.init_app(_app)
    mig.init_app(_app, db)
    loginmgr.init_app(_app)
    loginmgr.session_protection = "strong" #https://flask-login.readthedocs.io/en/latest/#session-protection
    loginmgr.login_view = 'login_blp.login' #Flask-Login needs to know what is the view function that handles logins.
    prcp.init_app(_app)
    admin_perm = Permission(RoleNeed("admin"))

    # Now initialize the database
    import commands
    commands.init_app(_app)

    # Register views
    from app1.views.index import index_blp
    from app1.views.login import login_blp
    from app1.views.register import register_blp
    from app1.views.oauth import oauth_blp
    from app1.views.oauth import github_blp
    from app1.views.api.v1_0 import api_v1_0_blp

    _app.register_blueprint(index_blp)
    _app.register_blueprint(login_blp)
    _app.register_blueprint(register_blp)
    _app.register_blueprint(oauth_blp)
    _app.register_blueprint(github_blp)
    _app.register_blueprint(api_v1_0_blp)
    # return
    # return app, db
    # print("[app1] Application created")
    return _app

# Init
# app, db = create_app()