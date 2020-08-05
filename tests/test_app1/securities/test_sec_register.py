# https://viblo.asia/p/tim-hieu-ve-sql-injection-testing-RQqKLv90l7z
import pytest
from bs4 import BeautifulSoup as bs
from flask import url_for

def test_register_sqlinjection(app, client):
    theurlstr = 'register_blp.reg'
    with app.test_request_context():
        # Test render without errors
        assert client.get(url_for(theurlstr)).status_code == 200
        # Test inject 1
        data = dict(
            inputName='2018 OR ""="',
            inputEmail='test@myflask.com OR ""="',
            inputPassword="123"
        )
        reg = client.post(url_for(theurlstr), data=data, follow_redirects=True)
        assert reg.status_code == 200 # has feedback
        assert reg.headers.get("Location") == None
        assert "Validation failed! Contact admin@myflask.com for help" in reg.data.decode('utf-8')
        assert '<script src="/static/js/login.js"></script>' not in reg.data.decode('utf-8') #not redirected to login
        
        data = dict(
            inputName='2018 OR ""="',
            inputEmail='test@myflask.com',
            inputPassword="123"
        )
        reg = client.post(url_for(theurlstr), data=data, follow_redirects=True)
        assert reg.status_code == 200 # has feedback
        assert reg.headers.get("Location") == None
        assert "Validation failed! Contact admin@myflask.com for help" in reg.data.decode('utf-8')
        assert '<script src="/static/js/login.js"></script>' not in reg.data.decode('utf-8') #not redirected to login
        
        data = dict(
            inputName='A test',
            inputEmail='test@myflask.com OR ""="',
            inputPassword="123"
        )
        reg = client.post(url_for(theurlstr), data=data, follow_redirects=True)
        assert reg.status_code == 200 # has feedback
        assert reg.headers.get("Location") == None
        assert "Validation failed! Contact admin@myflask.com for help" in reg.data.decode('utf-8')
        assert '<script src="/static/js/login.js"></script>' not in reg.data.decode('utf-8') #not redirected to login
        
        data = dict(
            inputName='A test',
            inputEmail="' OR 1=1",
            inputPassword="123"
        )
        reg = client.post(url_for(theurlstr), data=data, follow_redirects=True)
        assert reg.status_code == 200 # has feedback
        assert reg.headers.get("Location") == None
        assert "Validation failed! Contact admin@myflask.com for help" in reg.data.decode('utf-8')
        assert '<script src="/static/js/login.js"></script>' not in reg.data.decode('utf-8') #not redirected to login

        data = dict(
            inputName='A test',
            inputEmail='test@myflask.com; DROP TABLE tbl_users; --',
            inputPassword="123"
        )
        reg = client.post(url_for(theurlstr), data=data, follow_redirects=True)
        assert reg.status_code == 200 # has feedback
        assert reg.headers.get("Location") == None
        assert "Validation failed! Contact admin@myflask.com for help" in reg.data.decode('utf-8')
        assert '<script src="/static/js/login.js"></script>' not in reg.data.decode('utf-8') #not redirected to login

        # Test length of inputName (must be from 6-20)
        data = dict(
            inputName='A test i am the one who pass it alllllllllllllllllllllllllllll',
            inputEmail='test@myflask.com',
            inputPassword="123"
        )
        reg = client.post(url_for(theurlstr), data=data, follow_redirects=True)
        assert reg.status_code == 200 # has feedback
        assert reg.headers.get("Location") == None
        assert "Validation failed! Contact admin@myflask.com for help" in reg.data.decode('utf-8')
        assert '<script src="/static/js/login.js"></script>' not in reg.data.decode('utf-8') #not redirected to login
        
        data = dict(
            inputName='A',
            inputEmail='test@myflask.com',
            inputPassword="123"
        )
        reg = client.post(url_for(theurlstr), data=data, follow_redirects=True)
        assert reg.status_code == 200 # has feedback
        assert reg.headers.get("Location") == None
        assert "Validation failed! Contact admin@myflask.com for help" in reg.data.decode('utf-8')
        assert '<script src="/static/js/login.js"></script>' not in reg.data.decode('utf-8') #not redirected to login
        
        data = dict(
            inputName="'; select true; --",
            inputEmail='test@myflask.com',
            inputPassword="123"
        )
        reg = client.post(url_for(theurlstr), data=data, follow_redirects=True)
        assert reg.status_code == 200 # has feedback
        assert reg.headers.get("Location") == None
        assert "Validation failed! Contact admin@myflask.com for help" in reg.data.decode('utf-8')
        assert '<script src="/static/js/login.js"></script>' not in reg.data.decode('utf-8') #not redirected to login