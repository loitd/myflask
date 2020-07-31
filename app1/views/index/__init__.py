from flask import render_template, request, Response, json, session, redirect, url_for, abort, escape, flash, Blueprint
from werkzeug.security import generate_password_hash, check_password_hash
from lutils.utils import printlog, printwait
from app1.views.login import login_required

# https://flask.palletsprojects.com/en/1.1.x/blueprints/
# Define the BLUEPRINT here
index_blp = Blueprint('index_blp', __name__)

# @app.route('/', methods = ['GET'])
@index_blp.route('/', methods = ['GET'])
def index():
    if 'email' in session:
        _sessionemail = session['email']
        return render_template('home/index.html')
    else:
        return redirect(url_for('login_blp.getLogin'))
    
@index_blp.route('/profile', methods = ['GET'])
def profile():
    if 'email' in session:
        _sessionemail = session['email']
        user = {"email": _sessionemail}
        return render_template('home/profile.html', user=user)
    else:
        return redirect(url_for('login_blp.getLogin'))

@index_blp.route('/hello', methods=['GET'])
@login_required
def hello():
    return render_template('home/index.html')

        

    