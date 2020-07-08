from flask import Flask, current_app, g
import cx_Oracle
from lutils.lutils import printlog, printwait
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, static_folder = '../static', template_folder="../templates")
app.config.from_object('app1.config.DevelopmentConfig')

# DEFAULT database connection
# https://flask-sqlalchemy.palletsprojects.com/en/2.x/binds/
# MULTIPLE DATABASES for FLASK
# https://docs.sqlalchemy.org/en/13/core/engines.html#supported-databases
# Prod
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqldb://reportapi:NiDIFaXeDoCe7Ova7I3A4I33macOn6@172.16.213.18/test'
# Test/dev
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqldb://test:123456@localhost/test'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Oracle
# https://cx-oracle.readthedocs.io/en/latest/user_guide/connection_handling.html#connection-pooling
# e = create_engine("oracle+cx_oracle://user:pass@dsn?encoding=UTF-8&nencoding=UTF-8&mode=SYSDBA&events=true")
# SESSION issue with multiple database in Flask: https://stackoverflow.com/questions/38374005/flask-sqlalchemy-how-do-sessions-work-with-multiple-databases
# https://docs.sqlalchemy.org/en/13/orm/session_transaction.html#joining-a-session-into-an-external-transaction-such-as-for-test-suites
# Remember to release after using. 
app.config['SQLALCHEMY_BINDS'] = {
    'REPORTER':      'oracle+cx_oracle://PARTNERCTH:epay123123@172.16.10.81:1521/DB81',
    # 'REPORTER':      'oracle+cx_oracle://REPORTER:REPORTER123@DG1',
    'SQLITE':        'sqlite://', #in memory sqlite db
}
# Integrate to Flask app
db = SQLAlchemy(app)

# Production
# oraPool = cx_Oracle.SessionPool("REPORTER", "REPORTER123", "DG1", min=1, max=3, increment=1, encoding="UTF-8")
# Dev/Test
# oraPool = cx_Oracle.SessionPool("PARTNERCTH", "epay123123", "172.16.10.81:1521/DB81", min=1, max=3, increment=1, encoding="UTF-8")
# printlog("App & Database init done!", "monitordb.log")
# Local
oraPool = None

from app1.views.index import index_blp
from app1.views.login import login_blp
from app1.views.register import register_blp

app.register_blueprint(index_blp)
app.register_blueprint(login_blp)
app.register_blueprint(register_blp)