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

from flask import Flask, current_app
from lutils.utils import printlog, printwait
import os
from celery import Celery

_static = os.path.join(os.path.dirname(__file__), 'static')
_templates = os.path.join(os.path.dirname(__file__), 'templates')

app = Flask(__name__, static_folder = _static, template_folder=_templates)

# Check both this env exists and equals to
if os.environ.get("FLASK_ENV") and os.environ.get("FLASK_ENV").upper() == "PRODUCTION":
    app.config.from_object('app2.config.ProductionConfig')
elif os.environ.get("FLASK_ENV") and os.environ.get("FLASK_ENV").upper() == "DEVELOPMENT":
    app.config.from_object('app2.config.DevelopmentConfig')
else:
    app.config.from_object('app2.config.TestConfig')

# https://docs.celeryproject.org/en/stable/reference/celery.bin.worker.html#cmdoption-celery-worker-c
# celery -A app2.celery worker -c=2 -P threads -l info --autoscale=5,1 -E
# celery -A app2.celery worker -c=2 -P gevent -l info --autoscale=3,1 -E
celery = Celery(app.import_name)
celery.config_from_object('app2.config.CeleryConfig')
    
from app2.views.api.v1_0 import api_v1_0_blp

app.register_blueprint(api_v1_0_blp)
# return _app

# Init
# app, db = create_app()