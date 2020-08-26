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
# from flask_sqlalchemy import SQLAlchemy
# import os

# def configure_db(app):
    # DEFAULT database connection
    # https://flask-sqlalchemy.palletsprojects.com/en/2.x/binds/
    # MULTIPLE DATABASES for FLASK
    # https://docs.sqlalchemy.org/en/13/core/engines.html#supported-databases
    # app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqldb://reportapi:NiDIFaXeDoCe7Ova7I3A4I33macOn6@172.16.213.18/test'
    # # Test/dev
    # app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqldb://test:123456@localhost/test'
    # app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Oracle
    # https://cx-oracle.readthedocs.io/en/latest/user_guide/connection_handling.html#connection-pooling
    # e = create_engine("oracle+cx_oracle://user:pass@dsn?encoding=UTF-8&nencoding=UTF-8&mode=SYSDBA&events=true")
    # SESSION issue with multiple database in Flask: https://stackoverflow.com/questions/38374005/flask-sqlalchemy-how-do-sessions-work-with-multiple-databases
    # https://docs.sqlalchemy.org/en/13/orm/session_transaction.html#joining-a-session-into-an-external-transaction-such-as-for-test-suites
    # Production
    # oraPool = cx_Oracle.SessionPool("REPORTER", "REPORTER123", "DG1", min=1, max=3, increment=1, encoding="UTF-8")
    # Dev/Test
    # oraPool = cx_Oracle.SessionPool("PARTNERCTH", "epay123123", "172.16.10.81:1521/DB81", min=1, max=3, increment=1, encoding="UTF-8")
    # printlog("App & Database init done!", "monitordb.log")
    # Remember to release after using. 
    # app.config['SQLALCHEMY_BINDS'] = {
    #     'REPORTER':      'oracle+cx_oracle://PARTNERCTH:epay123123@172.16.10.81:1521/DB81',
    #     'REPORTER':      'oracle+cx_oracle://REPORTER:REPORTER123@DG1',
    #     'SQLITE':        'sqlite://', #in memory sqlite db
    # }
    
    # Integrate db to Flask app
    # return SQLAlchemy(app) #db

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