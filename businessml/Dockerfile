# This is a simple Dockerfile to use while developing
# It's not suitable for production
#
# It allows you to run both flask and celery if you enabled it
# for flask: docker run --env-file=.flaskenv image flask run
# for celery: docker run --env-file=.flaskenv image celery worker -A myapi.celery_app:app
#
# note that celery will require a running broker and result backend
FROM python:3.8-slim

RUN mkdir /code
WORKDIR /code

# COPY requirements.txt setup.py tox.ini ./
COPY requirements.txt ./
RUN pip install -U pip
RUN pip install -r requirements.txt

COPY businessml_api businessml_api/

EXPOSE 8000

ENTRYPOINT [ "python", "-m", "businessml_api.app", "" ]