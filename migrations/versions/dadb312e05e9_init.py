"""init

Revision ID: dadb312e05e9
Revises: 
Create Date: 2020-08-05 11:37:26.336862

"""
from alembic import op
import sqlalchemy as sa
from datetime import datetime
from sqlalchemy import exc
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
import pg8000

Session = sessionmaker()
Base = declarative_base()
bind = op.get_bind() #get bind engine
# A newly constructed Session may be said to be in the “begin” state. In this state, the Session has not established any connection or transactional state with any of the Engine objects that may be associated with it.
session = Session(bind=bind) # new session. No connections are in use. Waiting for 1st query.
# https://alembic.sqlalchemy.org/en/latest/ops.html
# https://docs.sqlalchemy.org/en/13/orm/session_transaction.html

# revision identifiers, used by Alembic.
revision = 'dadb312e05e9'
down_revision = None
branch_labels = None
depends_on = None

def drop_all_table():
    try:
        # Some platform like postgre FORCE us to COMMIT or ROLLBACK after each failed sql
        print("[drop_all_table] {0}".format(bind.engine.name))
        if bind.engine.name == "postgresql":
            print("[drop_all_table] Running on POSTGRESQL")
        # result = db.session.execute('SELECT * FROM my_table WHERE my_column = :val', {'val': 5})
        _sql = """DROP TABLE IF EXISTS tbl_user_role, tbl_users, tbl_roles CASCADE""" #RESTRICT: No drop if there's dependent object.
        _result = session.execute(_sql) #rowproxy.items() returns an array like [(key0, value0), (key1, value1)]
        print("[drop_all_table] {0}".format(_result))
        # For a clean init
        # ----------------------------------------------------------------------------------------------------
        # first query. A Connection is acquired from the Engine, and a Transaction started. 
        # session.begin_nested() # establish a savepoint
        # second query. The same Connection/Transaction are used.
        # session.rollback()  # rolls back u2, keeps u1
        # pending changes are created.
        # session.commit() # commits u1 and u2
        # ----------------------------------------------------------------------------------------------------
        # op.drop_table('tbl_user_role')
        # op.drop_table('tbl_users')
        # op.drop_table('tbl_roles')
        # commit. The pending changes above are flushed via flush(), the Transaction is committed, the Connection object closed and discarded, the underlying DBAPI connection returned to the connection pool.
        session.commit()
        print("[drop_all_table] Done")
    except Exception as e:
        print("[drop_all_table] EXCEPTION!!!")
        print(e)
        # on rollback, the same closure of state as that of commit proceeds.
        session.rollback() #ANY exception -> rollback
    finally:
        # close the Session. This will expunge any remaining objects as well as reset any existing SessionTransaction state. Neither of these steps are usually essential. 
        # However, if the commit() or rollback() itself experienced an unanticipated internal failure (such as due to a mis-behaved user-defined event handler), .close() will ensure that invalid state is removed.
        session.close()
        
def add_seed():
    print("[add_seed] Begin")
    tbl_roles = sa.sql.table( 'tbl_roles',
        sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
        sa.Column('role', sa.String(length=255), nullable=False),
        sa.Column('description', sa.String(length=500), nullable=True)
    )
    
    tbl_users = sa.sql.table('tbl_users',
        sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
        sa.Column('email', sa.String(length=255), nullable=False),
        sa.Column('password', sa.String(length=500), nullable=True),
        sa.Column('fullname', sa.String(length=255), nullable=False),
        sa.Column('status', sa.Integer(), nullable=False),
        sa.Column('authtype', sa.Integer(), nullable=False),
        sa.Column('created_date', sa.DateTime(timezone=True), nullable=False, default=datetime.utcnow),
        sa.Column('updated_date', sa.DateTime(timezone=True), nullable=False, default=datetime.utcnow)
    )
    
    tbl_user_role = sa.sql.table('tbl_user_role',
        sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
        sa.Column('user_email', sa.String(length=255), nullable=False),
        sa.Column('role_role', sa.String(length=255), nullable=False)
    )
    
    op.bulk_insert(
        tbl_roles,
        [
            {'role':'admin', 'description': 'Administrator'},
            {'role':'editor', 'description': 'Editor'},
            {'role':'user', 'description': 'Normal User'},
        ]        
    )
    
    op.bulk_insert(
        tbl_users,
        [
            {'email':'admin@myflask.com', 'password':"pbkdf2:sha256:150000$8MeWtFuN$22dd4d822ec9bc71d16841579a2bf4de92f2e2c3581341181627f7f96b03a647",'fullname':"Admin", 'status':1, 'authtype':0},
            {'email':'editor@myflask.com',  'password':"pbkdf2:sha256:150000$8MeWtFuN$22dd4d822ec9bc71d16841579a2bf4de92f2e2c3581341181627f7f96b03a647",'fullname':"Editor",  'status':1, 'authtype':0},
            {'email':'user@myflask.com',  'password':"pbkdf2:sha256:150000$8MeWtFuN$22dd4d822ec9bc71d16841579a2bf4de92f2e2c3581341181627f7f96b03a647",'fullname':"User",  'status':1, 'authtype':0},
        ]        
    )
    
    op.bulk_insert(
        tbl_user_role,
        [
            {'user_email':'admin@myflask.com', 'role_role': 'admin'},
            {'user_email':'user@myflask.com',  'role_role': 'user'},
            {'user_email':'editor@myflask.com', 'role_role': 'editor'},
        ]        
    )
    print("[add_seed] Done")


def upgrade():
    print("[upgrade] Begin")
    drop_all_table()
    # ### commands auto generated by Alembic - please adjust! ###
    print("[upgrade] Creating")
    op.create_table('tbl_roles',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('role', sa.String(length=255), nullable=False),
    sa.Column('description', sa.String(length=500), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('role')
    )
    op.create_table('tbl_users',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('email', sa.String(length=255), nullable=False),
    sa.Column('password', sa.String(length=500), nullable=True),
    sa.Column('fullname', sa.String(length=255), nullable=False),
    sa.Column('status', sa.Integer(), nullable=False),
    sa.Column('authtype', sa.Integer(), nullable=False),
    sa.Column('created_date', sa.DateTime(timezone=True), nullable=False, default=datetime.utcnow),
    sa.Column('updated_date', sa.DateTime(timezone=True), nullable=False, default=datetime.utcnow),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('tbl_user_role',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('user_email', sa.String(length=255), nullable=False),
    sa.Column('role_role', sa.String(length=255), nullable=False),
    sa.ForeignKeyConstraint(['role_role'], ['tbl_roles.role'], ),
    sa.ForeignKeyConstraint(['user_email'], ['tbl_users.email'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###
    add_seed()
    print("[upgrade] Done")


def downgrade():
    print("[downgrade] Begin")
    # ### commands auto generated by Alembic - please adjust! ###
    drop_all_table()
    # ### end Alembic commands ###
    print("[downgrade] Done")
