@ECHO OFF
IF ([%1] == []) (
	goto GIT
) 
IF ([%1] == ["setup"]) (
	goto SETUP
)

:SETUP
echo Do initial setup
REM python -m venv ./venv
pip install pipenv
pipenv install

:GIT
echo Do normal things
git pull origin master --allow-unrelated-histories
git add *
git commit -am "auto added and commited"
git push origin master