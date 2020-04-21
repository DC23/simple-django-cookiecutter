# -*- coding: utf-8 -*-

"""
This file contains all the settings used in production.
"""

from project.settings import config

# Production flags:
DEBUG = False

ALLOWED_HOSTS = [
    # TODO: check production hosts
    config("DOMAIN_NAME")
]

# Staticfiles
# https://docs.djangoproject.com/en/3.0/ref/contrib/staticfiles/

# Adding STATIC_ROOT to collect static files via 'collectstatic'
STATIC_ROOT = "/var/www/django/static"

# Mediafiles
MEDIA_ROOT = "/var/www/django/media"

# Security
# https://docs.djangoproject.com/en/3.0/topics/security/
SECURE_HSTS_SECONDS = 518400
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True

SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
SECURE_SSL_REDIRECT = True

SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

# Auth
LOGIN_REDIRECT_URL = config("LOGIN_REDIRECT_URL")
PATH_TO_PUBLIC_KEY = "REPLACE WITH PATH TO SSH PUBLIC KEY"
SSH_AUTH = "SSH KEY AUTHENTICATION"
