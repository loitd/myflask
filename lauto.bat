@ECHO OFF
REM This script is not active developed as moving to Circle CI
IF "%~1" == "" (
	GOTO GIT
) 
IF "%~1"=="setup" (
	GOTO SETUP
)
IF "%~1"=="run" (
	GOTO RUN
)
IF "%~1"=="test" (
	GOTO TEST
)
IF "%~1"=="deploy" (
	GOTO DEPLOY
)

:SETUP
ECHO Do initial setup
REM python -m pip install --upgrade pip
python -m venv ./venv && pip install -r requirements.txt
REM pip install pipenv
REM pipenv install
GOTO END

:GIT
ECHO Do normal things
git pull origin master --allow-unrelated-histories
git add *
git commit -am "lauto added and commited for minor fixes & features"
git push origin master
GOTO END

:DEPLOY
ECHO Deploy to heroku
git pull origin master --allow-unrelated-histories
git add *
git commit -am "lauto added and commited for minor fixes & features + deployment"
git push heroku master
GOTO END

:RUN
ECHO Run the app
REM SET FLASK_ENV=development
SET FLASK_ENV=test
venv\Scripts\activate && python ./main.py
GOTO END

:TEST
ECHO Run the app TEST
SET FLASK_ENV=test
venv\Scripts\activate && python -m pytest --cov=app1 --cov-report=xml --junitxml=test_reports/junit.xml && python -m codecov --token=5116b8f0-c09b-482b-b494-5fd66df4f6b3
REM venv\Scripts\activate && python -m pytest --cov=app1 -s
GOTO END

:END
echo All tasks done