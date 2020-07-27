from datetime import datetime
from sqlalchemy import Sequence, text
from sqlalchemy.orm import sessionmaker
from app1 import db

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