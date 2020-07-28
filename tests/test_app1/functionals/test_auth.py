import pytest
from app1.models import db
from flask import url_for, request

def test_unauth_access(client, theapp):
    # 302 Found redirect status response code indicates that the resource requested has been temporarily moved to the URL given by the Location header.
    assert client.get("/").status_code == 302
    # Because both request.base_url and url_for have / at the end and beginning -> slice last char of base_url
    assert client.get("/").headers.get("Location") == "{0}{1}".format(request.base_url[0:-1], url_for('login_blp.getLogin'))
    # yes, it is redirected

def test_login(client, theapp):
    # Test successful
    data = dict(
        inputEmail="admin@myflask.com",
        inputPassword="123456"
    )
    postLogin = client.post(url_for('login_blp.postLogin'), data=data, follow_redirects=True)
    assert postLogin.status_code == 200
    assert postLogin.headers.get("Location") == None
    # Test failed
    data = dict(
        inputEmail="admin@myflask.com",
        inputPassword="123"
    )
    postLogin = client.post(url_for('login_blp.postLogin'), data=data, follow_redirects=True)
    assert postLogin.status_code == 200

def test_register(client, theapp):
    # Test register new user with blank
    data = dict(
        inputName="",
        inputEmail="",
        inputPassword=""
    )
    postRegister = client.post(url_for('register_blp.postRegister'), data=data, follow_redirects=True)
    assert postRegister.status_code == 200
    # Test successful register
    data = dict(
        inputName="Johnny",
        inputEmail="john@myflask.com",
        inputPassword="123456"
    )
    postRegister = client.post(url_for('register_blp.postRegister'), data=data, follow_redirects=True)
    assert postRegister.status_code == 200