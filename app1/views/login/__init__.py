from flask import render_template, request, Response, json, session, redirect, url_for, abort, escape, flash, Blueprint, current_app
from werkzeug.security import generate_password_hash, check_password_hash
from app1.models.users import db, User
from app1.views import Const
from app1.models.authforms import LoginForm #use WTF
from flask_login import current_user, login_user, logout_user, login_required
from werkzeug.urls import url_parse

# Define the BLUEPRINT here
login_blp = Blueprint('login_blp', __name__)

@login_blp.route('/login', methods=['POST','GET'])
def login():
    try:
        if current_user.is_authenticated: 
            return redirect(url_for("index_blp.index"))
        form = LoginForm() #Declare WTF
        errors = [] #customized errors
        if request.method == "POST":  
            if form.validate_on_submit():
                _email = request.form.get('inputEmail', None)
                _password = request.form.get('inputPassword', None)
                hashedpassword = None
                if _email and _password:
                    row = db.session.query(User).filter_by(email=_email).first()
                    if row is not None: hashedpassword = row.password
                    # print(rows)
                    if row and check_password_hash(hashedpassword, _password) and hashedpassword:
                        # Successful
                        login_user(row)
                        # ---------------------
                        # Redirect to next page 
                        nextpage = request.args.get('next')
                        if not nextpage or url_parse(nextpage).netloc == '':
                            nextpage = url_for('index_blp.index')
                        return redirect(nextpage)
                    else:
                        # session.pop('_flashes', None) #Clear the flash message
                        errors.append(Const.MSG_USER_NOTFOUND)
            else:
                # for example, without CSRF
                errors.append(Const.MSG_VALIDATION_FAILED)
        return render_template('auth/login.html', form = form, errors=errors)
    except Exception as e:
        raise e
        print(e)
        
@login_blp.route('/login_v1_1', methods=['POST','GET'])
def login_v1_1():
    try:
        if request.method == "POST":
            errors = []
            _email = request.form.get('inputEmail', None)
            _password = request.form.get('inputPassword', None)
            hashedpassword = None
            if _email and _password:
                row = db.session.query(User).filter_by(email=_email).first()
                if row is not None: hashedpassword = row.password
                # print(rows)
                if row and check_password_hash(hashedpassword, _password) and hashedpassword:
                    session['email'] = _email
                    print("session set")
                    return redirect(url_for('index_blp.index'))
                else:
                    errors.append(Const.MSG_USER_NOTFOUND)
                    return render_template('auth/login.html', errors=errors)
                # print("Got: {0}, {1}".format(_email, _password))
            else:
                errors.append(Const.MSG_BLANK_FIELDS_SUBMITTED)
                return render_template('auth/login.html', errors=errors)
        elif request.method == "GET":
            if 'email' in session:
                return redirect(url_for('index_blp.index'))
            else:
                return render_template('auth/login.html')
    except Exception as e:
        raise(e)
        pass

@login_required
@login_blp.route('/logout', methods = ['GET'])
def getLogout():
    # session.pop('email', None)
    logout_user()
    return redirect(url_for('login_blp.login'))
