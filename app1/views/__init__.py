from flask import Flask, current_app, g
import cx_Oracle
from lutils.lutils import printlog, printwait
from app1.models import init_db

app = Flask(__name__, static_folder = '../static', template_folder="../templates")
app.config.from_object('app1.config.DevelopmentConfig')

# Init the database for app here
db = init_db(app)

# Local
oraPool = None

from app1.views.index import index_blp
from app1.views.login import login_blp
from app1.views.register import register_blp

app.register_blueprint(index_blp)
app.register_blueprint(login_blp)
app.register_blueprint(register_blp)