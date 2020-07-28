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
from app1.models import init_db

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
def db(app, request):
    """The db for the app"""
    init_db(app, _db)
    
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
        return self._client.post(url_for('login_blp.postLogin'), data=data)
    
    def logout(self):
        return self._client.get(url_for('login_blp.getLogout'))

@pytest.fixture(scope="session")
def auth(client):
    return AuthActions(client)