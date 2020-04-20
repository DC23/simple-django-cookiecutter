# -*- coding: utf-8 -*-

"""
This file contains all the settings that define the development server.

SECURITY WARNING: don't run with debug turned on in production!
"""

from project.settings import config
from project.settings.components.common import INSTALLED_APPS, MIDDLEWARE

# Setting the development status:
DEBUG = True

# Allowed hosts in dev mode
ALLOWED_HOSTS = ["0.0.0.0", "localhost", "127.0.0.1", "192.168.56.107"]

# Django debug toolbar
# See django-debug-toolbar.readthedocs.io
INSTALLED_APPS += ["debug_toolbar"]

# Debug toolbar docs recommend placing it close to the start of MIDDLEWARE list
MIDDLEWARE = ["debug_toolbar.middleware.DebugToolbarMiddleware"] + MIDDLEWARE

INTERNAL_IPS = ["0.0.0.0", "localhost", "127.0.0.1", "192.168.56.1"]

# This will make debug toolbar to work with django-csp,
# since `ddt` loads some scripts from `ajax.googleapis.com`:
# CSP_SCRIPT_SRC = ("'self'", "ajax.googleapis.com")
# CSP_IMG_SRC = ("'self'", "data:")

# Email
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
# EMAIL_BACKEND = "django.core.mail.backends.filebased.EmailBackend"
# EMAIL_FILE_PATH = "app-emails"

# Auth
# PATH_TO_PUBLIC_KEY = "REPLACE WITH PATH TO SSH PUBLIC KEY"
# SSH_AUTH = "SSH KEY AUTHENTICATION"

# Disable caching in development
CACHES = {
    "default": {"BACKEND": "django.core.cache.backends.dummy.DummyCache"},
}
CACHE_MIDDLEWARE_SECONDS = 0
