# {{ cookiecutter.project_name }} Developer's README

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

## TODO: Add your own README stuff...

## Directory layout

Rather than have all Django apps in the top level, they should be nested inside the project. E.G.:

```bash
# tree -L 3
.
├── deploy
│   ├── chef
│   └── docker
│       ├── devel
│       └── production
├── docs
├── logs
├── manage.py
├── media
├── project
│   ├── __init__.py
│   ├── apps
│   │   ├── auth
│   │   ├── blog
│   │   ├── faq
│   │   ├── pages
│   │   ├── portal
│   │   └── users
│   ├── conf
│   ├── settings.py
│   ├── static
│   ├── templates
│   ├── urls.py
│   └── wsgi.py
└── static
    └── admin
        ├── css
        ├── fonts
        ├── img
        └── js
```

Similarly, each app in the `/project/apps/` directory should follow a consistent layout:

```bash
# tree project/apps/portal/
project/apps/portal/
├── __init__.py
├── admin.py
├── apps.py
├── management
│   ├── __init__.py
│   └── commands
│       ├── __init__.py
│       └── update_portal_feeds.py
├── migrations
│   └── __init__.py
├── models.py
├── static
│   └── portal
│       ├── css
│       ├── img
│       └── js
├── templates
│   └── portal
│       └── index.html
├── templatetags
│   ├── __init__.py
│   └── portal.py
├── tests.py
├── urls.py
└── views.py
```

Specifically:

* *Static files*: `project/apps/appname/static/appname`
* *Template files*: `project/apps/appname/templates/appname`

The duplicated app name inside the `static` and `templates` directories is required because Django groups things into a common folder. This has the risk of name collisions if two different apps have a file with the same name. Including the app name in the path acts to namespace the files. See the [static files documentation](https://docs.djangoproject.com/en/3.0/howto/static-files/) for more details.

Using the suggested app structure helps keep the apps modular. With almost no changes an app could be pulled into a separate repo and published as a Python package.

## Local-host dev environment

### Install

1. Make sure you have Python {{ cookiecutter.min_python_version }} installed. This is specified in the Pipfile
2. Make sure you have [pipenv](https://pipenv.readthedocs.io/en/latest/) installed.
3. Then create the Python virtual environment with [Pipenv](https://pipenv.readthedocs.io/en/latest/):

```shell
pipenv install --dev
```

4. To install [`black`](https://github.com/psf/black) for code formatting, you need to install manually with pip after creating the main environment with pipenv. This is because `black` seems to be permanently in pre-release mode and I don't want to globally enable pre-releases in the `Pipfile`. The command is:

```shell
pipenv run pip install black
```

### Initial Database Setup

Create the initial migration and sync the database:

```shell
pipenv run python manage.py makemigrations
pipenv run python manage.py migrate
```

Now create a test user in your local database:

```shell
pipenv run python manage.py createsuperuser --email test@test.org --username admin
```

### Configuration

A distinction should be made between configuration settings that are the same for all instances of a project, and those that need to differ for each deployment. The former are here called "project settings" and the latter "instance settings".
This project uses two libraries to manage settings in a different manner to standard Django applications.

First, [django-split-settings](https://github.com/sobolevn/django-split-settings) is used to manage project settings in a modular way. Project settings are defined as a single Python module factored across multiple files. The top-level `__init__.py` file aggregates all the modules, and provides support for optional local overrides. Rather than have a single large file with all settings, they are broken out into separate files by category. All settings not currently broken into their own file are in `settings/components/common.py`.

Instance settings should be defined in a `config/settings.ini` file. The template can be used as a guide.
The `settings.ini` file should not be added to source control, to reduce the risk of production deployment with debug settings.
Alternatively, you can define corresponding environment variables, for example in a Dockerfile. Environment variables have precedence over values defined in the ini file.

Instance settings are loaded in the project settings files using the [python-decouple](https://github.com/henriquebastos/python-decouple) library. This library provides two key features over using `os.environ` to read directly from environment variables:

* Type safety. This avoids some common bugs and simplifies code when dealing with instance settings that are not strings.
* Guards against missing instance settings. Any instance setting that is not defined (either through configuration or a default value) will raise a `UndefinedValueError` on application launch.

See the python-decouple documentation for more details.

Usage is simple. Any configuration file that needs to load an instance setting must first import the `config` variable, and then use it to load the setting:

```python
from project.settings import config

# In production.py, no default value is defined
SECRET_KEY = config("DJANGO_SECRET_KEY")

SOME_SETTING = config("SOME_SETTING", default="abcde")

FTP_PORT= config("FTP_PORT", cast=int)
```

Note that in addition to the common production and development settings, you can create local settings overrides by creating a `project/settings/environments/local.py` file from the template. This file should not be added to source control.

### Running

```shell
pipenv run python manage.py runserver --nothreading --noreload
```

Or you can configure your IDE (VS Code has good Django support).

### Python Code Formatting

[Black](https://github.com/psf/black) is suggested for formatting all Python code. Prior to adding to Git, run:

```shell
black .
```
