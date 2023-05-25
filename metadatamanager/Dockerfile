# syntax=docker/dockerfile:1.4
# https://realpython.com/django-nginx-gunicorn/#starting-with-django-and-wsgiserver

FROM --platform=$BUILDPLATFORM python:alpine3.17 AS builder
EXPOSE 8000
WORKDIR /app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev

COPY requirements.txt /app
RUN pip3 install -r requirements.txt --no-cache-dir
COPY . /app

## django debug version
#ENTRYPOINT ["python3"]
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]

#gunicorn version
#ENV GUNICORN_CMD_ARGS="--bind=0.0.0.0"
#CMD [ "gunicorn", "metadatamanager.wsgi:application" ]



# FROM builder as dev-envs
# RUN <<EOF
# apk update
# apk add git
# EOF
#
# RUN <<EOF
# addgroup -S docker
# adduser -S --shell /bin/bash --ingroup docker vscode
# EOF
# # install Docker tools (cli, buildx, compose)
# COPY --from=gloursdocker/docker / /
# CMD ["manage.py", "runserver", "0.0.0.0:8000"]
