import pytest
from flask import url_for, session, request
from app1.models.users import User
from app1.views import Const

def test_unauth_access(app, client):
    # Wrap your thread code in a test_request_context so you have access to context locals:
    with app.test_request_context():
        # 302 Found redirect status response code indicates that the resource requested has been temporarily moved to the URL given by the Location header.
        assert client.get("/").status_code == 302
        # Because both request.base_url and url_for have / at the end and beginning -> slice last char of base_url
        assert client.get("/").headers.get("Location") == "{0}{1}".format(request.base_url[0:-1], url_for('login_blp.getLogin'))
        # yes, it is redirected

def test_login(app, client, db): #need DB to init the database for the test
    # Wrap your thread code in a test_request_context so you have access to context locals:
    with app.test_request_context():
        # Test render without errors
        assert client.get(url_for('login_blp.getLogin')).status_code == 200
        # Test NONE
        data = dict(
            inputEmail="",
            inputPassword=""
        )
        postLogin = client.post(url_for('login_blp.postLogin'), data=data, follow_redirects=True)
        assert postLogin.status_code == 200 # has feedback
        assert postLogin.headers.get("Location") == None # no redirection
        assert Const.MSG_BLANK_FIELDS_SUBMITTED in postLogin.data.decode("utf-8")
        
        # Test failed
        data = dict(
            inputEmail="admin@myflask.com",
            inputPassword="123"
        )
        postLogin = client.post(url_for('login_blp.postLogin'), data=data, follow_redirects=True)
        assert postLogin.status_code == 200 # has feedback
        assert postLogin.headers.get("Location") == None # no redirection
        assert Const.MSG_USER_NOTFOUND in postLogin.data.decode("utf-8")

def test_login_success(app, client, db):
    # Wrap your thread code in a test_request_context so you have access to context locals:
    with app.test_request_context():
        # Test successful
        data = dict(
            inputEmail="admin@myflask.com",
            inputPassword="123456"
        )
        postLogin = client.post(url_for('login_blp.postLogin'), data=data, follow_redirects=True)
        assert postLogin.status_code == 200 # has feedback
        assert postLogin.headers.get("Location") == None # no redirection
        assert Const.MSG_USER_NOTFOUND not in postLogin.data.decode("utf-8")
        # You have to logout or it will be redirected at register page
        # Test logout
        getLogout = client.get(url_for('login_blp.getLogout'), follow_redirects=True)
        assert getLogout.status_code == 200

def test_register(app, client, db):
    # Wrap your thread code in a test_request_context so you have access to context locals:
    with app.test_request_context():
        # Test render without errors
        assert client.get(url_for('register_blp.getRegister')).status_code == 200
        # Test register new user with blank
        data = dict(
            inputName="",
            inputEmail="",
            inputPassword=""
        )
        postRegister = client.post(url_for('register_blp.postRegister'), data=data, follow_redirects=True)
        assert postRegister.status_code == 200 # has feedback
        assert postRegister.headers.get("Location") == None # no redirection
        # Check response data for error message
        assert Const.MSG_BLANK_FIELDS_SUBMITTED in postRegister.data.decode("utf-8")
        
        # Test successful register
        data = dict(
            inputName="Johnny",
            inputEmail="john@myflask.com",
            inputPassword="123456"
        )
        postRegister = client.post(url_for('register_blp.postRegister'), data=data, follow_redirects=True)
        assert postRegister.status_code == 200 # has feedback
        # Susseccfully register -> redirected to login page
        assert postRegister.headers.get("Location") == None
        # Check if records exists in the database
        _row = db.session.query(User).filter_by(email=data["inputEmail"]).first()
        assert _row is not None #existed
        assert _row.email == data["inputEmail"]
        
        # Test duplicated user register
        data = dict(
            inputName="Johnny",
            inputEmail="john@myflask.com",
            inputPassword="123456"
        )
        postRegister = client.post(url_for('register_blp.postRegister'), data=data, follow_redirects=True)
        assert postRegister.status_code == 200 # has feedback
        assert postRegister.headers.get("Location") == None # no redirection
        assert Const.MSG_USER_EXISTED in postRegister.data.decode("utf-8")
    