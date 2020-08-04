from flask import render_template, request, Response, json, session, redirect, url_for, abort, escape, flash, Blueprint, current_app
from werkzeug.security import generate_password_hash, check_password_hash
from app1.models.users import db, User
from app1.views import Const
import requests
from oauthlib.oauth2 import WebApplicationClient
from flask_dance.contrib.github import make_github_blueprint, github
from flask_login import current_user, login_user, logout_user, login_required
from werkzeug.urls import url_parse

# Define the BLUEPRINT here
oauth_blp = Blueprint('oauth_blp', __name__)

# create blp
github_blp = make_github_blueprint(
    client_id=Const._GH_CLIENT_KEY,
    client_secret=Const._GH_CLIENT_SECRET,
    login_url="/oauth/gh/login", #the URL path for the login view. Defaults to /github
    authorized_url="/oauth/gh/authorized", #the URL path for the authorized view. Defaults to /github/authorized
    redirect_url="/oauth/gh", #the URL to redirect to after the authentication dance is complete
)

# OAuth 2 client setup
client = WebApplicationClient(Const._GG_CLIENT_ID)

def _social_login(email, fullname):
    # Here is for auth successfully
    # Write all information to the database
    row = db.session.query(User).filter_by(email=email).first()
    if row is None:
        # Not yet registered 
        row = User(email=email, password="", fullname=fullname, status=0, authtype=1)
        db.session.add(row)
        db.session.commit()
    login_user(row)
    nextpage = request.args.get('next')
    if not nextpage or url_parse(nextpage).netloc == '':
        nextpage = url_for('index_blp.index')
    return redirect(nextpage)

# @app.route('/login', methods=['GET'])
@oauth_blp.route('/oauth/gg', methods=['GET'])
def getGoogle():
    gg_provider_config = requests.get(Const._GG_DISCOVERY_URL).json()
    oauth_endpoint = gg_provider_config["authorization_endpoint"]
    # Use library to construct the request for Google login and provide
    # scopes that let you retrieve user's profile from Google
    request_uri = client.prepare_request_uri(
        oauth_endpoint,
        redirect_uri=request.base_url + "/callback",
        scope=["openid", "email", "profile"],
    )
    return redirect(request_uri)

@oauth_blp.route('/oauth/gg/callback', methods=['GET'])
def getGoogleCallback():
    # Get authorization code Google sent back to you
    code = request.args.get("code")
    # Find out what URL to hit to get tokens that allow you to ask for
    # things on behalf of a user
    gg_provider_config = requests.get(Const._GG_DISCOVERY_URL).json()
    token_endpoint = gg_provider_config["token_endpoint"]
    # Prepare and send a request to get tokens! Yay tokens!
    token_url, headers, body = client.prepare_token_request(
        token_endpoint,
        authorization_response=request.url,
        redirect_url=request.base_url,
        code=code
    )
    token_response = requests.post(
        token_url,
        headers=headers,
        data=body,
        auth=(Const._GG_CLIENT_ID, Const._GG_CLIENT_SECRET),
    )

    # Parse the tokens!
    client.parse_request_body_response(json.dumps(token_response.json()))
    # Now that you have tokens (yay) let's find and hit the URL
    # from Google that gives you the user's profile information,
    # including their Google profile image and email
    userinfo_endpoint = gg_provider_config["userinfo_endpoint"]
    uri, headers, body = client.add_token(userinfo_endpoint)
    userinfo_response = requests.get(uri, headers=headers, data=body)
    # You want to make sure their email is verified.
    # The user authenticated with Google, authorized your
    # app, and now you've verified their email through Google!
    if userinfo_response.json().get("email_verified"):
        unique_id = userinfo_response.json()["sub"]
        _email = userinfo_response.json()["email"]
        _picture = userinfo_response.json()["picture"]
        _name = userinfo_response.json()["given_name"]
    else:
        return "User email not available or not verified by Google.", 400
    # Here is for auth successfully
    # Write all information to the database
    return _social_login(email=_email, fullname=_name)

@oauth_blp.route('/oauth/gh', methods=['GET'])
def getGithub():
    if not github.authorized:
        return redirect(url_for("github.login"))
    resp = github.get("/user")
    assert resp.ok
    # return resp.json() # all got information
    _email = "{0}@github.com".format(resp.json()["login"])
    _name = resp.json()["name"]
    return _social_login(email=_email, fullname=_name) 