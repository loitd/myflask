from flask import render_template, request, Response, json, session, redirect, url_for, abort, escape, flash, Blueprint, current_app
from werkzeug.security import generate_password_hash, check_password_hash
from app1.models.users import db, User
from app1.views import Const
import requests
from oauthlib.oauth2 import WebApplicationClient

# Define the BLUEPRINT here
oauth_blp = Blueprint('oauth_blp', __name__)

# CONST
GG_CLIENT_ID="295954188669-rkk71kee7me6p5det62ruuu8vg91kd6f.apps.googleusercontent.com"
GG_CLIENT_SECRET="CUrSCZKHUvOtH-KoWh4AJiFS"
GG_DISCOVERY_URL="https://accounts.google.com/.well-known/openid-configuration"

# OAuth 2 client setup
client = WebApplicationClient(GG_CLIENT_ID)

# @app.route('/login', methods=['GET'])
@oauth_blp.route('/oauth/gg', methods=['GET'])
def getGoogle():
    gg_provider_config = requests.get(GG_DISCOVERY_URL).json()
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
    gg_provider_config = requests.get(GG_DISCOVERY_URL).json()
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
        auth=(GG_CLIENT_ID, GG_CLIENT_SECRET),
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
    row = db.session.query(User).filter_by(email=_email).first()
    if row is None:
        # Not yet registered 
        _usr = User(email=_email, password="", fullname=_name, status=0, authtype=1)
        db.session.add(_usr)
        db.session.commit()
    # login
    session['email'] = _email
    # print("session set")
    return redirect(url_for('index_blp.index'))
    