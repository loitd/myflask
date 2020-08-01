from flask import Blueprint
# https://flask.palletsprojects.com/en/1.1.x/blueprints/
# Define the BLUEPRINT here
api_v1_0_blp = Blueprint('api_v1_0_blp', __name__)

from app1.views.api.v1_0.jobs import *