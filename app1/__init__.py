# Moving all app1 general to here
# Instead of placing at Views

from flask import Flask, current_app
from lutils.utils import printlog, printwait
from flask_sqlalchemy import SQLAlchemy
import os

_static = os.path.join(os.path.dirname(__file__), 'static')
_templates = os.path.join(os.path.dirname(__file__), 'templates')

app = Flask(__name__, static_folder = _static, template_folder=_templates)

# Check both this env exists and equals to
if os.environ.get("FLASK_ENV") and os.environ.get("FLASK_ENV").upper() == "PRODUCTION":
    app.config.from_object('app1.config.ProductionConfig')
elif os.environ.get("FLASK_ENV") and os.environ.get("FLASK_ENV").upper() == "DEVELOPMENT":
    app.config.from_object('app1.config.DevelopmentConfig')
else:
    app.config.from_object('app1.config.TestConfig')

# Init the database for app here
db = SQLAlchemy(app)

# Now initialize the database
from app1.models import init_db
init_db()

# Register views
from app1.views.index import index_blp
from app1.views.login import login_blp
from app1.views.register import register_blp

app.register_blueprint(index_blp)
app.register_blueprint(login_blp)
app.register_blueprint(register_blp)
# return
# return app, db
print("[app1] Application created")