# --------------------------------------------------------------------------------
# Warning: this commandline to create database seeds NO LONGER being maintained. 
# Use MIGRATE instead
# --------------------------------------------------------------------------------
import click
from sqlalchemy import text
from app1 import db
from app1.models.users import User
from app1.models.roles import Role
from app1.models.user_role import UserRole

def create_db():
    """Creates database"""
    db.create_all()
    
def drop_db():
    """Cleans database"""
    db.drop_all()

def create_model_table():
    """ Create table model in the database """
    Model.__table__.create(db.engine)

def add_seed():
    """Add initial seed data for dbs"""
    drop_db()
    create_db()
    # create an administrator user
    _u = [
        Role(role="admin", description="Administrator permissions"),
        Role(role="user", description="Normal User permissions"),
        User(email="admin@myflask.com", password="pbkdf2:sha256:150000$8MeWtFuN$22dd4d822ec9bc71d16841579a2bf4de92f2e2c3581341181627f7f96b03a647", fullname="Admin", status=1, authtype=0),
        User(email="user@myflask.com", password="pbkdf2:sha256:150000$8MeWtFuN$22dd4d822ec9bc71d16841579a2bf4de92f2e2c3581341181627f7f96b03a647", fullname="Normal User", status=1, authtype=0),
        UserRole(user_email="admin@myflask.com", role_role="admin"),
        UserRole(user_email="user@myflask.com", role_role="user"),
    ]
    # db.session.add(_u)
    db.session.bulk_save_objects(_u)
    db.session.commit()
    print("[add_seed] Database initialized!")
    UserRole.createTest()
    return True

# Factory pattern
def init_app(app):
    # add multiple commands in a bulk
    for command in [create_db, drop_db, create_model_table, add_seed]:
        app.cli.add_command(app.cli.command()(command))