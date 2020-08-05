# content of test_checkconfig.py
import pytest
import os

def test_env():
    assert os.environ.get("FLASK_ENV") == "test"
    assert os.environ.get("FLASK_APP") == "app1"
    assert os.environ.get("GH_CLIENT_KEY") is not None
    assert os.environ.get("GH_CLIENT_SECRET") is not None
    assert os.environ.get("GG_CLIENT_ID") is not None
    assert os.environ.get("GG_CLIENT_SECRET") is not None

def test_config(app):
    assert app.config["ENV"] == 'test'
    assert app.config["TESTING"] == True
    assert app.config["SECRET_KEY"] is not None
    assert app.config["SQLALCHEMY_DATABASE_URI"] is not None
    assert app.config["WTF_CSRF_ENABLED"] == False # turn off CSRF