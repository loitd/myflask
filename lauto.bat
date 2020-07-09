@ECHO OFF
IF "%~1" == "" (
	GOTO GIT
) 
IF "%~1"=="setup" (
	GOTO SETUP
)
IF "%~1"=="run" (
	GOTO RUN
)
IF "%~1"=="shell" (
	GOTO SHELL
)

:SETUP
ECHO Do initial setup
REM python -m pip install --upgrade pip
REM python -m venv ./venv
pip install pipenv
pipenv install
GOTO END

:GIT
ECHO Do normal things
git pull origin master --allow-unrelated-histories
git add *
git commit -am "auto added and commited"
git push origin master
GOTO END

:RUN
ECHO Run the app
pipenv run python ./main.py
GOTO END

:SHELL
ECHO Run the app SHELL
set FLASK_APP=main
pipenv run flask shell
GOTO END

:END
echo All tasks done