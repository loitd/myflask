'''
Created Date: Monday August 24th 2020
Author: Leo Tran (https://github.com/loitd)
-----
Last Modified: Monday August 24th 2020 8:28:38 pm
Modified By: Leo Tran (https://github.com/loitd)
-----
HISTORY:
Date      	By    	Comments
----------	------	---------------------------------------------------------
25-08-2020	loitd	Initialize the file
'''

from flask import render_template, request, Response, json, session, redirect, url_for, abort, escape, flash, Blueprint, jsonify
import time
from app2 import celery
from celery import group, chain, chord
# https://flask.palletsprojects.com/en/1.1.x/blueprints/
# Define the BLUEPRINT here
api_v1_0_blp = Blueprint('api_v1_0_blp', __name__)

# http://localhost:5000/api/v1_0/add/100/200
@api_v1_0_blp.route('/api/v1_0/add/<a>/<b>', methods=['GET','POST'])
def celeryAdd(a,b):
    if request.method == 'GET':
        res = add.delay(a,b) #call a simple celery task
        # print("did the add")
        while not res.ready(): #block until got result
            pass
        _ret = {"result": 200, "msg": "Added value: {0}".format(res.get(timeout=3)), "htmlmsg": "Method(s) <b>not</b> allowed"}
    elif request.method == "POST":
        pass
    return jsonify(_ret)

# http://localhost:5000/api/v1_0/add2/100/200
@api_v1_0_blp.route('/api/v1_0/add2/<a>/<b>', methods=['GET','POST'])
def celeryAdd2(a,b):
    if request.method == 'GET':
        res = add2.delay(a,b) #call a simple celery task
        _ret = """  <p>result: 200</p>
                    <p>msg: "Added value is calculating at task ID: {0}"</p>
                    <p>htmlmsg: <a href="/api/v1_0/status/{0}">{0}</a></p>""".format(res.id)
    # return jsonify(_ret)
    return _ret

# http://localhost:5000/api/v1_0/add3/100/200
@api_v1_0_blp.route('/api/v1_0/add3/<a>/<b>', methods=['GET','POST'])
def celeryAdd3(a,b):
    """This is for a specific Celery workflow
    f = (a+b) * (a+b)
    We'll use chord, group and chain"""
    if request.method == 'GET':
        # When a worker receives an expired task it will mark the task as REVOKED
        res = (group(add.s(a,b), add.s(a,b)) | mul.s()).apply_async(expires=60) #https://docs.celeryproject.org/en/stable/userguide/calling.html#expiration
        _ret = """  <p>result: 200</p>
                    <p>msg: "Added value is calculating at task ID: {0}"</p>
                    <p>htmlmsg: <a href="/api/v1_0/status/{0}">{0}</a></p>""".format(res.id)
    # return jsonify(_ret)
    return _ret

# http://localhost:5000/api/v1_0/status/taskid
@api_v1_0_blp.route('/api/v1_0/status/<taskid>', methods=['GET'])
def celeryAddStatus(taskid):
    if request.method == 'GET':
        res = add2.AsyncResult(taskid) #https://docs.celeryproject.org/en/stable/reference/celery.result.html
        # print(res.info) #Task return value
        if res and res.state != 'FAILURE':
            total = res.info.get('total', 0)
            percent = res.info.get('percent', 0)
            status = res.status
            children = res.children
            _ret = {"result": 200, "taskid": taskid, "msg": "STATUS: {3} - TOTAL: {1} - PERCENT: {2} - CHILDREN: {4}".format(taskid, total, percent, status, children)}
        else:
            _ret = {"result": 500, "msg": "Task ID: {0} - TOTAL: - - PERCENT: -".format(taskid)}
    return jsonify(_ret)

# runs in a Celery worker process
@celery.task
def add(a,b):
    time.sleep(3)
    return int(a)+int(b)

@celery.task(bind=True)
def mul(self, ls):
    self.update_state(state='PENDING', meta={'total': 0, 'percent': 0.25})
    time.sleep(3)
    return {'total': int(ls[0])*int(ls[1]), 'percent': 1.00}

# runs in a Celery worker process: state = PENDING|STARTED|RETRY|FAILURE|SUCCESS
@celery.task(bind=True)
def add2(self, a,b):
    """When doing the update, the message will look like this:
    {'task_id': '5660d3a3-92b8-40df-8ccc-33a5d1d680d7',
    'result': {'percent': 50, 'total': 20},
    'children': [],
    'status': 'PENDING',
    'traceback': None}
 """
    self.update_state(state='PENDING', meta={'total': int(a)/4+int(b)/4, 'percent': 0.25})
    time.sleep(10)
    self.update_state(state='PENDING', meta={'total': int(a)/2+int(b)/2, 'percent': 0.50})
    time.sleep(10)
    return {'total': int(a)+int(b), 'percent': 1.00}

# Celery Worklow Primitives
# https://docs.celeryproject.org/en/stable/userguide/canvas.html
# https://www.ovh.com/blog/doing-big-automation-with-celery/#:~:text=Celery%20natively%20supports%20combining%20such,%2C%20chords%2C%20etc.).&text=The%20elementary%20tasks%20can%20be,%E2%80%9D%2C%20and%20%E2%80%9Cchord%E2%80%9D.
# Chain – a set of tasks processed sequentially
# Group – a set of tasks processed in parallel
# Chord – a group of tasks chained to the following task

