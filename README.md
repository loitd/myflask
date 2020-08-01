# myflask
[![codecov](https://codecov.io/gh/loitd/myflask/branch/master/graph/badge.svg)](https://codecov.io/gh/loitd/myflask)
[![lutils](https://circleci.com/gh/loitd/myflask.svg?style=svg)](https://circleci.com/gh/loitd/myflask)  
My Python Flask Template with: 
* Modular Flask with Blueprint
* Pre-configured SQLAlchemy ORM (to MySQL, Oracle, SQLite, Postgres)
* Frontend with Bootstrap 4
* Coding, testing and deploying automated using CI/CD with Pytest, Codecov, Circle CI, Heroku.
* Social authentications beside classic email/password.
* Backend API with Flask
* Dockerized with Dockerfile (guide below)
## Links
* Demo: [https://loi-flask.herokuapp.com/](https://loi-flask.herokuapp.com/)
* Page: [https://loitd.github.io/myflask/](https://loitd.github.io/myflask/)
* Github: [https://github.com/loitd/myflask](https://github.com/loitd/myflask)
## Installation
This is how to install this template:  
### Linux
* `git clone https://github.com/loitd/myflask.git`  
* `cd myflask`  
* `python -m venv venv`
* `source venv/bin/activate`
* `(venv) pip install -r requirements.txt`  
* `(venv) export FLASK_APP=app1`
* `(venv) export FLASK_ENV=test`
* `(venv) export GH_CLIENT_KEY=******`
* `(venv) export GH_CLIENT_SECRET=******`
* `(venv) export GG_CLIENT_ID=******`
* `(venv) export GG_CLIENT_SECRET=******`
* `(venv) flask add-seed`  
* `(venv) flask run`  
### Docker
* Clone to your local:  
`git clone https://github.com/loitd/myflask && cd myflask`  
* Create the MariaDB container (root password will be printed to console):  
* `sudo docker run --name mariadb -d -e MYSQL_RANDOM_ROOT_PASSWORD=yes -e MYSQL_DATABASE=myflask -e MYSQL_USER=myflask -e MYSQL_PASSWORD=mypassword mariadb:10.5`  
* Check with `sudo docker ps` command  
* Build `myflask` image from Dockerfile:  
* `sudo docker build -t myflask:latest .`  
* Check with `sudo docker images` command  
* Run a container for that image (mapping host port 9001 to container port 5000 + remove when terminated):  
* `sudo docker run -d -p 9001:5000 --rm myflask:latest -e GH_CLIENT_KEY=xxx -e GH_CLIENT_SECRET=xxx -e GG_CLIENT_ID=xxx -e GG_CLIENT_SECRET=xxx -e SQLALCHEMY_DATABASE_URI=mysql+pymysql://myflask:mypassword@localhost/myflask`  
## Notes
* `Python 3.7` is recommended
* `Python 3.7.8` tested with
* Do NOT use `mysqlclient==2.0.1` since it has problem installing on Docker. Moved to `PyMySQL==0.10.0`.  
* Do NOT use `psycopg2==2.8.5` since it has problem installing on Docker. Moved to `pg8000==1.16.3`.  
* In any case, keep ONLY ONE of `Pipfile` or `requirements.txt` in your project.  
* To setup data base and data seed on Heroku:  
    - Select run console  
    ![Run console](https://github.com/loitd/myflask/blob/master/heroku-config-01.png?raw=true)
    - Run `flask add-seed` command just like in the dev/test env  
    ![Run console](https://github.com/loitd/myflask/blob/master/heroku-config-02.png?raw=true)