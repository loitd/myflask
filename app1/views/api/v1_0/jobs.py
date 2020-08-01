from flask import render_template, request, Response, json, session, redirect, url_for, abort, escape, flash, Blueprint, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from lutils.utils import printlog, printwait
from app1.views.login import login_required
from lutils.utils import printwait
from app1.views.api.v1_0 import api_v1_0_blp
from app1.views.api import exetime_decor

@api_v1_0_blp.route('/api/v1_0/swich', methods=['GET','POST'])
@exetime_decor
def swich_v1_0():
    printwait("[swich_v1_0] Processing command now", 1, "myflask_api.log")
    if request.method == 'GET':
        _ret = {"result": 500, "msg": "Method(s) not allowed", "htmlmsg": "Method(s) <b>not</b> allowed"}
    elif request.method == "POST":
        _cmd = request.form.get("cmd")
        _ret = {"result": 200, "msg": "Your command: {0} has been executed successfully".format(_cmd), "htmlmsg": 'Your command: <b>{0}</b> has been executed <b><span style="color: green;">successfully</span></b>'.format(_cmd)}
    return jsonify(_ret)


    

    