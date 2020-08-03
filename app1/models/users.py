from datetime import datetime
from sqlalchemy import Sequence, text
from sqlalchemy.orm import sessionmaker
from werkzeug.security import generate_password_hash
from app1 import db, loginmgr
from flask_login import UserMixin

class User(UserMixin, db.Model):
    __tablename__ = 'tbl_users'
    __bind_key__ = None # No Bind Key -> default db
    id = db.Column(db.Integer, Sequence('user_id_seq'), primary_key=True, autoincrement=True)
    email = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(500), nullable=True) #loggin in by Google/Twitter -> empty password
    fullname = db.Column(db.String(255), nullable=False)
    status = db.Column(db.Integer, nullable=False, default=0) #0: not confirmed email, 1 confirmed
    authtype = db.Column(db.Integer, nullable=False, default=0) #0: normal, 1: google, 2: facebook, 3: twitter, 4: github
    # created_date = db.Column(db.DateTime(timezone=True), default=datetime.now, nullable=False)
    created_date = db.Column(db.DateTime(timezone=True), default=datetime.utcnow, nullable=False)
    updated_date = db.Column(db.DateTime(timezone=True), default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)
    
    def __repr__(self):
        return '<USER %r>' % self.email

@loginmgr.user_loader
def get_user(id):
    """Because Flask-Login knows nothing about databases, it needs the application's help in loading a user. 
    For that reason, the extension expects that the application will configure a user loader function, that can be called to load a user given the ID.
    The user loader is registered with Flask-Login with the @login.user_loader decorator."""
    return User.query.get(int(id))








