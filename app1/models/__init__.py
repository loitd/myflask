# You need to use one of the following commands. Which one depends on what OS and software you have and use.
# easy_install mysql-python (mix os)
# pip install mysql-python (mix os/ python 2)
# pip install mysqlclient (mix os/ python 3)
# apt-get install python-mysqldb (Linux Ubuntu, ...)
# cd /usr/ports/databases/py-MySQLdb && make install clean (FreeBSD)
# yum install MySQL-python (Linux Fedora, CentOS ...)
# For Windows, see this answer: Install mysql-python (Windows)

# https://docs.sqlalchemy.org/en/13/core/engines.html
# You may need to RE-LOGIN to see result of db.create_all() and db.drop_all() command with from models import db

from app1.views import db
from datetime import datetime
from sqlalchemy import Sequence, text
from sqlalchemy.orm import sessionmaker

class User(db.Model):
    __tablename__ = 'tbl_users'
    __bind_key__ = None # No Bind Key -> default db
    id = db.Column(db.Integer, Sequence('user_id_seq'), primary_key=True, autoincrement=True)
    email = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(500), nullable=False)
    fullname = db.Column(db.String(255), nullable=False)
    status = db.Column(db.Integer, nullable=False, default=0)
    # created_date = db.Column(db.DateTime(timezone=True), default=datetime.now, nullable=False)
    created_date = db.Column(db.DateTime(timezone=True), default=datetime.utcnow, nullable=False)
    updated_date = db.Column(db.DateTime(timezone=True), default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)
    
    def __repr__(self):
        return '<USER %r>' % self.email

class DB81User(db.Model):
    __tablename__ = 'DB81_USERS' #name must be different to distinguised
    __bind_key__ = 'REPORTER'
    id = db.Column(db.Integer, Sequence('DB81_USER_ID_SEQ'), primary_key=True)
    email = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(555), nullable=False)
    fullname = db.Column(db.String(255), nullable=False)
    status = db.Column(db.Integer, nullable=False, default=0)
    created_date = db.Column(db.DateTime(timezone=True), default=datetime.utcnow, nullable=False)
    updated_date = db.Column(db.DateTime(timezone=True), default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)
    
    def __repr__(self):
        return '<REPORTER_USER %r>' % self.email
    

# Create all tables for default
# db.create_all()
# db.create_all(bind=['DB81'])

# New ORM User
# _u = DB81User(email="a@a.com", password="123", fullname="Nguyen Van A", status=0)

# Create a SEPARATED SESSION for Reporter db
# reporter_session = db.session(bind='REPORTER')
# OR
# reporter_engine = db.get_engine(bind='REPORTER')
# print(reporter_engine) #to check
# Session = sessionmaker(bind=reporter_engine)
# reporter_session = Session()

# Execute a NON_ORM sql
# rows = reporter_engine.execute(text("SELECT * FROM SYM_USERS"))
# print("Here is rows:")
# for row in rows:
#     print(row)

# Start a transaction in this session + catch Errors
# https://docs.sqlalchemy.org/en/13/core/connections.html?highlight=transaction#sqlalchemy.engine.Engine.begin
# Return a context manager delivering a Connection with a Transaction established.
# Upon successful operation, the Transaction is committed. If an error is raised, the Transaction is rolled back.
# https://docs.sqlalchemy.org/en/13/orm/session_transaction.html
# try:
    # reporter_session.begin_nested() # establish a savepoint but ONLY works with NON-ORM queries
    # reporter_session.add(_u)
    # reporter_session.commit()
    # print("Commited")
# except Exception as e:
    # print("Exception")
    # print(e.orig)
    # print("Ex")
    # print(e.params)
#     if "ORA-00001: unique constraint (PARTNERCTH.SYS_C0038447) violated" in str(e.orig):
#         print("User email exists")
#     reporter_session.flush()
#     reporter_session.rollback()
# finally:
#     reporter_session.close()

