# pipenv install pytest
# pipenv install setup\coverage-5.2-cp37-cp37m-win_amd64.whl
# https://flask.palletsprojects.com/en/1.1.x/testing/#the-testing-skeleton
# https://pypi.org/project/coverage/#files

#------------------------------------------------------------------------------------
# Import from parent folder
# import sys
# sys.path.append('../components')
# from core import GameLoopEvents
#------------------------------------------------------------------------------------
import os
import tempfile
import pytest
from app1 import app, db
from app1.models import init_db

@pytest.fixture(scope="session")
def client():
    """We create the app and db for TEST env"""
    with app.test_client() as client:
        with app.app_context():
            init_db()
        yield client

@pytest.fixture(scope="session")
def theapp():
    return app