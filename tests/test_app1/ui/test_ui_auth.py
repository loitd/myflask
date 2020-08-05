import pytest
from bs4 import BeautifulSoup as bs
from flask import url_for

def test_register_has_form(app, client):
    with app.test_request_context():
        # 302 Found redirect status response code indicates that the resource requested has been temporarily moved to the URL given by the Location header.
        assert client.get(url_for('register_blp.reg')).status_code == 200
        _getReg = client.get(url_for('register_blp.reg'))
        _html = _getReg.data.decode("utf-8")
        assert 'form class="form-signin" id="formRegister" method="POST"' in _html
        _soup = bs(_html, "html.parser")
        _forms = _soup.find_all("form")
        assert len(_forms) == 1 #only 1 form
        try:
            form_action = _forms[0].attrs.get("method").lower()
        except Exception as e:
            form_action = None
        assert form_action is not None
        assert form_action == "post"
        
def test_register_has_assets(app, client):
    with app.test_request_context():
        # 302 Found redirect status response code indicates that the resource requested has been temporarily moved to the URL given by the Location header.
        assert client.get(url_for('register_blp.reg')).status_code == 200
        _getReg = client.get(url_for('register_blp.reg'))
        _html = _getReg.data.decode("utf-8")
        assert '<img class="mb-4" src="/static/img/kcal.svg" alt="" width="72" height="72">' in _html #logo
        assert '<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>' in _html #jquery
        assert '<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/css/bootstrap.min.css' in _html #bootstrap css
        assert '<script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/js/bootstrap.min.js' in _html #bootstrap js
        assert '<script src="https://cdn.jsdelivr.net/npm/feather-icons@4.28.0/dist/feather.min.js' in _html #feather js
        assert '<link rel="stylesheet" href="/static/css/register.css">' in _html #css
        assert '<script src="/static/js/register.js"></script>' in _html #js

def test_login_has_form(app, client):
    with app.test_request_context():
        # 302 Found redirect status response code indicates that the resource requested has been temporarily moved to the URL given by the Location header.
        assert client.get(url_for('login_blp.login')).status_code == 200
        _getReg = client.get(url_for('login_blp.login'))
        _html = _getReg.data.decode("utf-8")
        assert 'form class="form-signin" id="formRegister" method="POST"' not in _html
        assert '<form class="form-signin" id="formLogin" method="POST"' in _html
        assert '<a href="/oauth/gg" class="btn btn-lg btn-danger btn-block">Login with Google</a>' in _html
        assert '<a href="/oauth/gh" class="btn btn-lg btn-secondary btn-block">Login with Github</a>' in _html
        _soup = bs(_html, "html.parser")
        _forms = _soup.find_all("form")
        assert len(_forms) == 1 #only 1 form
        try:
            form_action = _forms[0].attrs.get("method").lower()
        except Exception as e:
            form_action = None
        assert form_action is not None
        assert form_action == "post"
        
def test_login_has_assets(app, client):
    with app.test_request_context():
        # 302 Found redirect status response code indicates that the resource requested has been temporarily moved to the URL given by the Location header.
        assert client.get(url_for('login_blp.login')).status_code == 200
        _getReg = client.get(url_for('login_blp.login'))
        _html = _getReg.data.decode("utf-8")
        assert '<img class="mb-4" src="/static/img/kcal.svg" alt="" width="72" height="72">' in _html #logo
        assert '<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>' in _html #jquery
        assert '<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/css/bootstrap.min.css' in _html #bootstrap css
        assert '<script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/js/bootstrap.min.js' in _html #bootstrap js
        assert '<script src="https://cdn.jsdelivr.net/npm/feather-icons@4.28.0/dist/feather.min.js' in _html #feather js
        assert '<link rel="stylesheet" href="/static/css/login.css">' in _html #css
        assert '<script src="/static/js/login.js"></script>' in _html #js
