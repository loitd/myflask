from datetime import datetime
from sqlalchemy import Sequence, text
from sqlalchemy.orm import sessionmaker, relationship
from app1 import db, loginmgr

# https://flask-sqlalchemy.palletsprojects.com/en/2.x/models/

class UserRole(db.Model):
    __tablename__ = 'tbl_user_role'
    __bind_key__ = None # No Bind Key -> default db
    id = db.Column(db.Integer, Sequence('userrole_id_seq'), primary_key=True, autoincrement=True)
    user_email = db.Column(db.String(255), db.ForeignKey('tbl_users.email'), nullable=False)
    role_role = db.Column(db.String(255), db.ForeignKey('tbl_roles.role'), nullable=False) #register & login capable    
    
    def __repr__(self):
        return '<USER_ROLE %r>' % self.email

    def createTest(self, email='', role=''):
        sql = text('SELECT * FROM tbl_users')
        rows = db.engine.execute(sql)
        print(rows)
        return rows


# user_role = db.Table('tbl_user_role',
#     db.Column('user_email', db.String(255), db.ForeignKey('tbl_users.email'), nullable=False),
#     db.Column('role_role', db.String(255), db.ForeignKey('tbl_roles.role'), nullable=False)  
# )



