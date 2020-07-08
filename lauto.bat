@ECHO OFF
if [%1] == [] (
	goto GIT
)

:SETUP
REM setup
REM python -m venv ./venv
pip install pipenv
pipenv install

:GIT
git pull origin master --allow-unrelated-histories
git add *
git commit -am "auto added and commited"
git push origin master