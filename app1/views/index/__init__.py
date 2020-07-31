from flask import render_template, request, Response, json, session, redirect, url_for, abort, escape, flash, Blueprint, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from lutils.utils import printlog, printwait
from app1.views.login import login_required
from lutils.utils import printwait

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

@index_blp.route('/api/v1.0/swich', methods=['GET','POST'])
def swich_v1_0():
    printwait("[swich_v1_0]", 3, "myflask_api.log")
    if request.method == 'GET':
        _ret = {"result": 500, "msg": "Method(s) not allowed", "htmlmsg": "Method(s) <b>not</b> allowed"}
    elif request.method == "POST":
        _cmd = request.form.get("cmd")
        _ret = {"result": 200, "msg": "Your command: {0} has been executed successfully".format(_cmd), "htmlmsg": 'Your command: <b>{0}</b> has been executed <b><span style="color: green;">successfully</span></b>'.format(_cmd)}
    return jsonify(_ret)

        

    