from datetime import datetime
from sqlalchemy import Sequence, text
from sqlalchemy.orm import sessionmaker
from app1 import db, loginmgr

class Role(db.Model):
    __tablename__ = 'tbl_roles'
    __bind_key__ = None # No Bind Key -> default db
    id = db.Column(db.Integer, Sequence('role_id_seq'), primary_key=True, autoincrement=True)
    role = db.Column(db.String(255), unique=True, nullable=False)
    description = db.Column(db.String(500), nullable=True)
    
    def __repr__(self):
        return '<ROLE %r>' % self.role