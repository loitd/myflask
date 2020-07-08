from flask import render_template, request, Response, json, session, redirect, url_for, abort, escape, flash, Blueprint, current_app
from werkzeug.security import generate_password_hash, check_password_hash
from app1.models import db, User

# Define the BLUEPRINT here
login_blp = Blueprint('login_blp', __name__)

def login_required(view):
    """View decorator that redirects anonymous users to the login page. Its a general TEMPLATE."""
    def inner(*args, **kwargs):
        # if email is not in session -> redirect
        if 'email' not in session: return render_template('auth/login.html')
        # else return view with all args
        return view(*args, **kwargs)
    return inner

# @app.route('/login', methods=['GET'])
@login_blp.route('/login', methods=['GET'])
def getLogin():
    if 'email' in session:
        return redirect(url_for('index_blp.index'))
    else:
        return render_template('auth/login.html')

# @app.route('/login', methods=['POST'])
@login_blp.route('/login', methods=['POST'])
def postLogin():
    try:
        errors = []
        _email = request.form.get('inputEmail', None)
        _password = request.form.get('inputPassword', None)
        hashedpassword = None
        row = db.session.query(User).filter_by(email=_email).first()
        if row is not None: hashedpassword = row.password
        # print(rows)
        if row and check_password_hash(hashedpassword, _password) and hashedpassword:
            session['email'] = _email
            print("session set")
            return redirect(url_for('index_blp.index'))
        else:
            errors.append("Username and password combination not found.")
            return render_template('login.html', errors=errors)
        print("Got: {0}, {1}".format(_email, _password))
    except Exception as e:
        raise(e)
        pass

# @app.route('/logout', methods = ['GET'])
@login_blp.route('/logout', methods = ['GET'])
def getLogout():
    session.pop('email', None)
    return redirect(url_for('index_blp.index'))
