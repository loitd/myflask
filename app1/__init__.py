# Moving all app1 general to here
# Instead of placing at Views

from flask import Flask, current_app
from lutils.utils import printlog, printwait
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os

_static = os.path.join(os.path.dirname(__file__), 'static')
_templates = os.path.join(os.path.dirname(__file__), 'templates')

db = SQLAlchemy()
mig = Migrate()

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

    # Now initialize the database
    from app1.models import init_db
    init_db(_app, db)

    # Register views
    from app1.views.index import index_blp
    from app1.views.login import login_blp
    from app1.views.register import register_blp

    _app.register_blueprint(index_blp)
    _app.register_blueprint(login_blp)
    _app.register_blueprint(register_blp)
    # return
    # return app, db
    print("[app1] Application created")
    return _app

# Init
# app, db = create_app()