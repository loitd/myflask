#!/bin/bash
# Make this entrypoint of Docker
# docker run -d myflask -e GH_CLIENT_KEY=xxx -e GH_CLIENT_SECRET=xxx -e GG_CLIENT_ID=xxx -e GG_CLIENT_SECRET=xxx
venv/bin/flask add-seed 
venv/bin/gunicorn wsgi -b :5000 --access-logfile - --error-logfile -