from datetime import datetime
from sqlalchemy import Sequence, text
from sqlalchemy.orm import sessionmaker
from werkzeug.security import generate_password_hash
from app1.views import db

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
    
    def __init__(self):
        self.db = db
        db.create_all()
    
    def __repr__(self):
        return '<USER %r>' % self.email








