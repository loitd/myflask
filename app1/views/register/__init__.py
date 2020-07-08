from flask import render_template, request, Response, json, session, redirect, url_for, abort, escape, flash, Blueprint, current_app
from werkzeug.security import generate_password_hash, check_password_hash
from app1.models import db, User

# Define the BLUEPRINT here
register_blp = Blueprint('register_blp', __name__)

# @app.route('/reg', methods = ['GET'])
@register_blp.route('/reg', methods = ['GET'])
def getRegister():
    if 'email' in session:
        return redirect(url_for('index_blp.index'))
    else:
        return render_template('auth/signup.html')

# @app.route('/reg', methods = ['POST'])
@register_blp.route('/reg', methods = ['POST'])
def postRegister():
    try:
        # print("Begin processing postRegister")
        errors = []
        _name = request.form.get('inputName', None)
        _email = request.form.get('inputEmail', None)
        _password = request.form.get('inputPassword', None)
        _hashpassword = generate_password_hash(_password)
        print("Got: {0}, {1}, {2}, {3}".format(_name, _email, _password, _hashpassword))
        if _name and _email and _password:
            row = db.session.query(User).filter_by(email=_email).first()
            if row and row.email == _email:
                errors.append("Email already exists.")
                print(errors)
                return render_template('signup.html', errors=errors)
            else:
                _usr = User(email=_email, password=_hashpassword, fullname=_name, status=0)
                db.session.add(_usr)
                db.session.commit()
                return redirect(url_for('login_blp.getLogin'))
    except Exception as e:
        raise(e)
        print(e)