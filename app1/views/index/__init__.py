from flask import render_template, request, Response, json, session, redirect, url_for, abort, escape, flash, Blueprint, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from lutils.utils import printlog, printwait
from flask_login import login_required
from lutils.utils import printwait
from app1.models.perms import admin_perm, editor_perm, user_perm

# https://flask.palletsprojects.com/en/1.1.x/blueprints/
# Define the BLUEPRINT here
index_blp = Blueprint('index_blp', __name__)

# @app.route('/', methods = ['GET'])
@index_blp.route('/', methods = ['GET'])
@index_blp.route('/index', methods = ['GET'])
@login_required
# @admin_perm.require(http_exception=403)
def index():
    return render_template('home/index.html')
    
@index_blp.route('/profile', methods = ['GET'])
@login_required
def profile():
    return render_template('home/profile.html')

@index_blp.route('/hello', methods=['GET'])
@login_required
def hello():
    return render_template('home/index.html')

@index_blp.route('/admin', methods = ['GET'])
# @login_required
@admin_perm.require(http_exception=403)
def admin():
    return render_template('home/admin.html')

@index_blp.route('/editor', methods = ['GET'])
# @login_required
@editor_perm.require(http_exception=403)
def editor():
    return render_template('home/editor.html')

@index_blp.errorhandler(403)
def authorisation_failed(e):
    return redirect(url_for("index_blp.page403"))

@index_blp.route('/403', methods=['GET'])
def page403():
    return render_template("common/permission_denied.html")
