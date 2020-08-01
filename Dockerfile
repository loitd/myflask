# https://goinbigdata.com/docker-run-vs-cmd-vs-entrypoint/
FROM python:3.7-slim

RUN adduser -D myflask

WORKDIR /home/myflask

COPY requirements.txt requirements.txt
RUN python -m venv venv
RUN venv/bin/pip install -r requirements.txt
RUN venv/bin/pip install gunicorn

COPY app1 app1
COPY migrations migrations
COPY wsgi.py boot.sh ./
RUN chmod +x boot.sh

ENV FLASK_APP app1

RUN chown -R myflask:myflask ./
USER myflask

EXPOSE 5000
ENTRYPOINT ["./boot.sh"]