# https://goinbigdata.com/docker-run-vs-cmd-vs-entrypoint/
FROM python:3.7-slim

RUN adduser myflask

WORKDIR /home/myflask

COPY requirements.txt requirements.txt
RUN python -m venv venv 
RUN venv/bin/pip install -r requirements.txt

COPY app1 app1
COPY commands commands
COPY wsgi.py boot.sh ./
RUN chmod +x boot.sh

ENV FLASK_APP app1
ENV FLASK_ENV development

# RUN chown -R myflask:myflask ./
# USER myflask

EXPOSE 5000
ENTRYPOINT ["/bin/bash", "boot.sh"]