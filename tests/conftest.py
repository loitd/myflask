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
from app1.views import app

@pytest.fixture
def client():
    """We create a pytest fixture called client() that configures the application for testing and initializes a new database.
    https://docs.pytest.org/en/latest/fixture.html
    Software test fixtures initialize test functions. This client fixture will be called by each individual test. 
    It gives us a simple interface to the application, where we can trigger test requests to the application. 
    The client will also keep track of cookies for us."""
    
    # Because SQLite3 is filesystem-based, we can easily use the tempfile module to create a temporary database and initialize it. 
    # The mkstemp() function does two things for us: it returns a LOW-LEVEL FILE HANDLE and a random FILE NAME, the latter we use as DATABASE NAME. 
    # We just have to keep the db_fd around so that we can use the os.close() function to close the file.
    db_fd, app.config['DATABASE'] = tempfile.mkstemp()
    
    # During setup, the TESTING config flag is activated. 
    # What this does is disable error catching during request handling, so that you get better error reports when performing test requests against the application.
    app.config['TESTING'] = True

    with app.test_client() as client:
        with app.app_context():
            app.init_db()
        yield client

    # To delete the database after the test, the fixture closes the file and removes it from the filesystem.
    os.close(db_fd)
    os.unlink(app.config['DATABASE'])
    # we now run the test suite with pytest command