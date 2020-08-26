# myflask
[![codecov](https://codecov.io/gh/loitd/myflask/branch/master/graph/badge.svg)](https://codecov.io/gh/loitd/myflask)
[![lutils](https://circleci.com/gh/loitd/myflask.svg?style=svg)](https://circleci.com/gh/loitd/myflask)
[![](https://img.shields.io/github/v/release/loitd/myflask?include_prereleases)](https://img.shields.io/github/v/release/loitd/myflask?include_prereleases)
[![](https://img.shields.io/github/repo-size/loitd/myflask)](https://img.shields.io/github/repo-size/loitd/myflask)
## Links
* Demo: [https://loi-flask.herokuapp.com/](https://loi-flask.herokuapp.com/)
* Page: [https://loitd.github.io/myflask/](https://loitd.github.io/myflask/)
* Github: [https://github.com/loitd/myflask](https://github.com/loitd/myflask) 
My Python Flask Template with:  
APP1  
* Modular Flask with Blueprint
* Pre-configured [SQLAlchemy ORM](https://flask-sqlalchemy.palletsprojects.com/en/2.x/) (to MySQL, Oracle, SQLite, Postgres)
* Fully responsive using frontend with [Bootstrap 4](http://getbootstrap.com/), [Chart.js](https://www.chartjs.org/docs/latest/), [FeatherIcon](https://feathericons.com/)
* Coding, testing and deploying automated using CI/CD with [Pytest](https://docs.pytest.org/en/stable/), [Codecov](https://docs.codecov.io/docs/python), [Circle CI](https://circleci.com/), [Heroku](https://loi-flask.herokuapp.com/).
* Social authentications beside classic email/password.
* Backend API with Flask
* Dockerized with Docker Compose (guide below)
* CSRF protection/Form validation with [Flask-WTF](http://packages.python.org/Flask-WTF/)
* Login Manager with [Flask-Login](https://flask-login.readthedocs.org/en/latest/)
* RBAC with [Flask-Principle](http://packages.python.org/Flask-Principal/)
* Migrated with [Flask-Migrate]() from v1.2 (was commandline before)
* SQLInjection prevention with tips at [this](https://realpython.com/prevent-python-sql-injection/#executing-a-query) and [this](https://viblo.asia/p/tim-hieu-ve-sql-injection-testing-RQqKLv90l7z) and [this](https://www.thepythoncode.com/code/sql-injection-vulnerability-detector-in-python). Security tests provided in `tests/test_app1/securities/` folder. (from v1.2)
* Performance tests with [Locust](https://docs.locust.io/en/stable/quickstart.html) (from v1.2) with Failures ratio ~ 8%
    - `locust -f tests\test_app1\performance\test_perf_locust.py`  
APP2  
* API with [Celery asynchronous task queue](https://docs.celeryproject.org/en/stable/) (Redis as broker & result backend, gevent or threads)
    - Pre-configured + samples Celery with Flask with status update
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
* `(venv) flask db upgrade`  
* `(venv) flask run`  
### Docker
* Clone to your local:  
`git clone https://github.com/loitd/myflask && cd myflask`   
* Update your keys pre-configured with samples at `docker-compose.yml`  
* Turn the whole up with `docker-compose`: `sudo docker-compose up`  
## Notes
* `Python 3.7` is recommended
* `Python 3.7.8` tested with
* Do NOT use `mysqlclient==2.0.1` since it has problem installing on Docker. Moved to `PyMySQL==0.10.0`. Modify database URL to: `mysql+pymysql://...`  
* Do NOT use `psycopg2==2.8.5` since it has problem installing on Docker. Moved to `pg8000==1.16.3`. Then in the database URL, modify to: `postgresql+pg8000://...`  
* You can NOT run `source venv/bin/activate` command in Docker. You need to specify to `venv/bin/flask` for EVERY Python command.  
* In any case, keep ONLY ONE of `Pipfile` or `requirements.txt` in your project.  
* To setup data base and data seed on Heroku:  
    - Select run console  
    ![Run console](https://github.com/loitd/myflask/blob/master/heroku-config-01.png?raw=true)
    - Run `flask add-seed` command just like in the dev/test env  
    ![Run console](https://github.com/loitd/myflask/blob/master/heroku-config-02.png?raw=true)
    - Wait until you see this text in the console: `[add_seed] Database initialized!`  
* `flask add-seed` command gives you all database setup and 2 default users with default password `123456` for both:
    - `admin@myflask.com` as an administrator account  
    - `user@myflask.com` as a normal user account  
## For developers
* List of APIs:
    - `/api/v1_0/swich`: Command management
    - `/api/v1_0/updateuser`: User profile management (for frontend)
* Push to Docker hub
    - switch to `root`  
    - `docker login`  
    - `docker images`
    - `docker push imagename`  
* Rebuild if any change:  
    - `sudo docker-compose build`
* About Migration: [Introduction](https://github.com/loitd/myflask/blob/master/migration.md)
* More performance tests:
    - ![Perf Test](https://github.com/loitd/myflask/blob/master/myflask_locust_perf_test.png?raw=true)  
    - ![Perf Test](https://github.com/loitd/myflask/blob/master/response_times_ms_1596651398.png?raw=true)
    - ![Perf Test](https://github.com/loitd/myflask/blob/master/total_requests_per_second_1596651397.png?raw=true)
## License
* [License](https://github.com/loitd/myflask/blob/master/LICENSE)