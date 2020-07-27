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
    data = dict(
        username="admin@myflask.com",
        password="123456"
    )
    assert client.post(url_for('login_blp.getLogin'), data=data, follow_redirects=True).status_code == 200
    assert client.post(url_for('login_blp.getLogin'), data=data, follow_redirects=True).headers.get("Location") == None