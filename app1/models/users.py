from datetime import datetime
from sqlalchemy import Sequence, text
from sqlalchemy.orm import sessionmaker, relationship
from werkzeug.security import generate_password_hash
from app1 import db, loginmgr
from flask_login import UserMixin

# https://flask-sqlalchemy.palletsprojects.com/en/2.x/models/

class User(UserMixin, db.Model):
    __tablename__ = 'tbl_users'
    __bind_key__ = None # No Bind Key -> default db
    id = db.Column(db.Integer, Sequence('user_id_seq'), primary_key=True, autoincrement=True)
    email = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(500), nullable=True) #loggin in by Google/Twitter -> empty password
    fullname = db.Column(db.String(255), nullable=False)
    status = db.Column(db.Integer, nullable=False, default=0) #0: not confirmed email, 1 confirmed
    # role = db.Column(db.String(255), db.ForeignKey('tbl_roles.role'), nullable=False, default="user") #register & login capable
    authtype = db.Column(db.Integer, nullable=False, default=0) #0: normal, 1: google, 2: facebook, 3: twitter, 4: github
    # created_date = db.Column(db.DateTime(timezone=True), default=datetime.now, nullable=False)
    created_date = db.Column(db.DateTime(timezone=True), default=datetime.utcnow, nullable=False)
    updated_date = db.Column(db.DateTime(timezone=True), default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)
    # Relationship
    # roles = db.relationship('Role', secondary=roles, lazy='joined', backref=db.backref('tbl_users', lazy=True))
    
    def __repr__(self):
        return '<USER %r>' % self.email
    
    def getRoles(self):
        # print(self.id)
        _sql = text("""SELECT A.role_role FROM tbl_user_role A WHERE A.user_email = '{0}'""".format(self.email))
        rows = db.engine.execute(_sql)
        _roles = [row[0] for row in rows]
        print(_roles)
        return _roles

@loginmgr.user_loader
def get_user(id):
    """Because Flask-Login knows nothing about databases, it needs the application's help in loading a user. 
    For that reason, the extension expects that the application will configure a user loader function, that can be called to load a user given the ID.
    The user loader is registered with Flask-Login with the @login.user_loader decorator."""
    return User.query.get(int(id))








