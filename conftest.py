# pipenv install pytest
# pipenv install setup\coverage-5.2-cp37-cp37m-win_amd64.whl
# https://flask.palletsprojects.com/en/1.1.x/testing/#the-testing-skeleton
# https://pypi.org/project/coverage/#files
# 
#------------------------------------------------------------------------------------
# This setup based on: http://alexmic.net/flask-sqlalchemy-pytest/
#------------------------------------------------------------------------------------
import os
import tempfile
import pytest
from app1 import create_app
from app1 import db as _db
from app1.models.users import User
from app1.models.roles import Role
from app1.models.user_role import UserRole

@pytest.fixture(scope="session")
def app(request):
    app = create_app() 
    
    # Its very important step to prevent AssertionError: Popped wrong app context. ERROR
    # Remove the application context after each test
    ctx = app.app_context()
    ctx.push()
    
    def teardown():
        ctx.pop()
    
    request.addfinalizer(teardown) #yes, tear it down for me!
    return app
    
@pytest.fixture(scope="session")
def client(app):
    """We create the app and db for TEST env"""
    return app.test_client()

@pytest.fixture(scope="session")
def cli(app):
    """We create the app and db for TEST env"""
    return app.test_cli_runner()



@pytest.fixture(scope="session")
def db(app, request):
    """The db for the app"""
    _db.drop_all()
    _db.create_all()
    _u = [
        Role(role="admin", description="Administrator permissions"),
        Role(role="editor", description="Editor permissions"),
        Role(role="user", description="Normal User permissions"),
        User(email="admin@myflask.com", password="pbkdf2:sha256:150000$8MeWtFuN$22dd4d822ec9bc71d16841579a2bf4de92f2e2c3581341181627f7f96b03a647", fullname="Admin", status=1, authtype=0),
        User(email="editor@myflask.com", password="pbkdf2:sha256:150000$8MeWtFuN$22dd4d822ec9bc71d16841579a2bf4de92f2e2c3581341181627f7f96b03a647", fullname="Editor", status=1, authtype=0),
        User(email="user@myflask.com", password="pbkdf2:sha256:150000$8MeWtFuN$22dd4d822ec9bc71d16841579a2bf4de92f2e2c3581341181627f7f96b03a647", fullname="Normal User", status=1, authtype=0),
        UserRole(user_email="admin@myflask.com", role_role="admin"),
        UserRole(user_email="editor@myflask.com", role_role="editor"),
        UserRole(user_email="user@myflask.com", role_role="user"),
    ]
    _db.session.bulk_save_objects(_u)
    _db.session.commit()
    pass
    # _db.session.add(_u)
    # _db.session.commit()
    
    def teardown():
        _db.drop_all()
    
    request.addfinalizer(teardown) #again
    return _db
    
class AuthActions:
    def __init__(self, client):
        self._client = client
    
    def login(self, email="admin@myflask.com", password="123456"):
        data = dict(
            inputEmail=email,
            inputPassword=password
        )
        return self._client.post(url_for('login_blp.login'), data=data)
    
    def logout(self):
        return self._client.get(url_for('login_blp.getLogout'))

@pytest.fixture(scope="session")
def auth(client):
    return AuthActions(client)