# -*- coding: utf-8 -*-

"""
Django settings for server project.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their config, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

from django.utils.translation import ugettext_lazy as _
from project.settings import config, BASE_DIR, ENV

# To avoid cylic dependencies, the SECRET_KEY needs to be defined here so that
# it can be imported into other settings files. If it is defined in the
# environment files then it can be hard to access the value in settings files that
# are parsed before the environment files.
# Note that prod does not have a default value.
if ENV == "production":
    SECRET_KEY = config("DJANGO_SECRET_KEY")
else:
    SECRET_KEY = config(
        "DJANGO_SECRET_KEY",
        default="#(=6k@f2#%d%nkv21*%r=8r#%=edt^83lnlk5#yla8(i!!=i0w",
    )

# Application title used in templates
SITE_NAME = "CSIRO Carbon Spec Database"

# Application definition:

INSTALLED_APPS = [
    # Local project apps:
    "project.apps.main",
    # Default django apps:
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # django-admin:
    "django.contrib.admin",
    "django.contrib.admindocs",
    # HTML and CSS helper apps:
    "bootstrap4",
    "django_icons",
    # 'django_filters',
    # Security:
    # 'axes',
    "corsheaders",
    # Other:
    "django_extensions",
    # TODO: Determine if Django FSM is required
    # "django_fsm",
]

MIDDLEWARE = [
    # Django:
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "django.middleware.locale.LocaleMiddleware",
    "django.contrib.admindocs.middleware.XViewMiddleware",
    # Security:
    "corsheaders.middleware.CorsMiddleware",
]

ROOT_URLCONF = "project.urls"

WSGI_APPLICATION = "project.wsgi.application"


# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = False
USE_L10N = False
USE_TZ = True
LANGUAGES = (("en", _("English")),)
LOCALE_PATHS = ("locale/",)


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/
STATIC_URL = "/static/"

STATICFILES_FINDERS = (
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
)

# Templates
# https://docs.djangoproject.com/en/3.0/ref/templates/api
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "APP_DIRS": True,
        "DIRS": [
            # Contains plain text templates, like `robots.txt`:
            BASE_DIR.joinpath("project", "templates").as_posix()
        ],
        "OPTIONS": {
            "context_processors": [
                # Default template context processors:
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "django.template.context_processors.debug",
                "django.template.context_processors.i18n",
                "django.template.context_processors.media",
                "django.template.context_processors.request",
                "django_settings_export.settings_export",
            ]
        },
    }
]

# Media files
# Media-root is commonly changed in production
# (see development.py and production.py).

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR.joinpath("media").as_posix()
