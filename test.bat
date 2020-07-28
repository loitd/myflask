@ECHO OFF
REM You can not run pytest command directly. You must run by python -m pytest command.
pipenv run python -m pytest
REM pipenv run coverage run -m pytest
REM pipenv run coverage report
REM open htmlcov/index.html in a browser
REM pipenv run coverage html