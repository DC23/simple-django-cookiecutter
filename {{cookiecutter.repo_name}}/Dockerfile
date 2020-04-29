# Dockerfile for sas_api

# Creates an empty database. If you want to use an existing database,
# pass it in as a volume.

# Outputs the dependencies as a requirements file and then installs them so we don't need to run
# inside a virtualenv. This makes the deployment with wsgi a little easier.

# TODO: Testing: it should be possible to run the tests in this container by
# running 'python manage.py test instance.tests' and passing in
# AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, and possibly AWS_SESSION_TOKEN to
# the container's environment.
# for google auth to work, you need to pass in more environment variables,
# see sas_api/settings/production.py for details.

# Runs the app under Apache's mod_wsgi, as is mentioned in the Django
# deployment instructions.

FROM python:{{ cookiecutter.min_python_version }}

ARG HASH=""

# open container spec labels
# https://github.com/opencontainers/image-spec/blob/master/annotations.md#back-compatibility-with-label-schema

LABEL org.opencontainers.image.revision="${HASH}"
LABEL org.opencontainers.image.source="{{ cookiecutter.repo_url }}"
LABEL org.opencontainers.image.title="{{ cookiecutter.repo_name }}"

RUN \
    apt-get update && \
    apt-get -y install apache2 apache2-dev && \
    pip install mod_wsgi pipenv && \
    useradd \
        --create-home \
        --home-dir /app \
        --no-log-init \
        --system \
        --group www-data \
        --uid 700 \
        --shell /bin/bash \
        django

WORKDIR /app

COPY --chown=django:www-data . .

RUN pipenv install --system

USER django

RUN \
    python manage.py makemigrations api && \
    python manage.py migrate

ENV COMMIT ${HASH}
