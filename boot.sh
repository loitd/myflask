#!/bin/sh
# Make this entrypoint of Docker
# docker run -it myflask -e GH_CLIENT_KEY=xxx -e GH_CLIENT_SECRET=xxx -e GG_CLIENT_ID=xxx -e GG_CLIENT_SECRET=xxx
source venv/bin/activate
export FLASK_ENV=test
export FLASK_APP=app1
flask add-seed
# flask translate compile
exec gunicorn wsgi -b :5000 --access-logfile - --error-logfile -