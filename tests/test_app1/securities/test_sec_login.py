# https://viblo.asia/p/tim-hieu-ve-sql-injection-testing-RQqKLv90l7z
import pytest
from bs4 import BeautifulSoup as bs
from flask import url_for

def test_login_sqlinjection(app, client):
    theurlstr = 'login_blp.login'
    with app.test_request_context():
        # Test render without errors
        assert client.get(url_for(theurlstr)).status_code == 200
        # Test inject 1
        data = dict(
            inputEmail='test@myflask.com OR ""="',
            inputPassword="123"
        )
        reg = client.post(url_for(theurlstr), data=data, follow_redirects=True)
        assert reg.status_code == 200 # has feedback
        assert reg.headers.get("Location") == None
        assert "Validation failed" in reg.data.decode('utf-8')
        assert '<script src="/static/js/dashboard.js"></script>' not in reg.data.decode('utf-8') #not redirected to login
        
        data = dict(
            inputEmail='" OR 1=1',
            inputPassword="123"
        )
        reg = client.post(url_for(theurlstr), data=data, follow_redirects=True)
        assert reg.status_code == 200 # has feedback
        assert reg.headers.get("Location") == None
        assert "Validation failed" in reg.data.decode('utf-8')
        assert '<script src="/static/js/dashboard.js"></script>' not in reg.data.decode('utf-8') #not redirected to login

        data = dict(
            inputEmail='test@myflask.com; DROP TABLE tbl_users; --',
            inputPassword="123"
        )
        reg = client.post(url_for(theurlstr), data=data, follow_redirects=True)
        assert reg.status_code == 200 # has feedback
        assert reg.headers.get("Location") == None
        assert "Validation failed" in reg.data.decode('utf-8')
        assert '<script src="/static/js/dashboard.js"></script>' not in reg.data.decode('utf-8') #not redirected to login