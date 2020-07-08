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
echo Do normal things
git pull origin master --allow-unrelated-histories
git add *
git commit -am "auto added and commited"
git push origin master