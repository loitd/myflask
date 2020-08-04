from flask import render_template, request, Response, json, session, redirect, url_for, abort, escape, flash, Blueprint, current_app
from werkzeug.security import generate_password_hash, check_password_hash
from app1.models.users import db, User
from app1.views import Const
from app1.models.authforms import RegisterForm #use WTF
from flask_login import current_user, login_user, logout_user, login_required
from werkzeug.urls import url_parse
import time

# Define the BLUEPRINT here
register_blp = Blueprint('register_blp', __name__)

@register_blp.route('/reg', methods = ['POST','GET'])
def reg():
    try:
        # session.pop('_flashes', None) #Clear the flash message
        if current_user.is_authenticated:
            return redirect(url_for("index_blp.index"))
        form = RegisterForm()
        errors = []
        if request.method == "POST": 
            if form.validate_on_submit():
                _name = request.form.get('inputName', None)
                _email = request.form.get('inputEmail', None)
                _password = request.form.get('inputPassword', None)
                # print("Got: {0}, {1}, {2}, {3}".format(_name, _email, _password))
                if _name and _email and _password:
                    _hashpassword = generate_password_hash(_password)
                    row = db.session.query(User).filter_by(email=_email).first()
                    if row and row.email == _email:
                        errors.append(Const.MSG_USER_EXISTED) #existed
                    else:
                        _usr = User(email=_email, password=_hashpassword, fullname=_name, status=0)
                        db.session.add(_usr)
                        db.session.commit()
                        # flash("Registered successfully. Please login with your new account.")
                        return redirect(request.args.get('next') or url_for('login_blp.login'))
                else:
                    errors.append(Const.MSG_BLANK_FIELDS_SUBMITTED)
            else:
                errors.append(Const.MSG_VALIDATION_FAILED)
        return render_template('auth/signup.html', errors=errors, form=form)
    except Exception as e:
        raise(e)
        print(e)