# -*- coding: utf-8 -*-

# Django authentication system
# https://docs.djangoproject.com/en/3.0/topics/auth/

from datetime import timedelta

from project.settings.components.common import SECRET_KEY

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",},
]

# configure authentication
LOGIN_URL = "login"
LOGIN_REDIRECT_URL = "/"
# LOGOUT_REDIRECT_URL = "/"
AUTH_USER_MODEL = "main.User"

# appropriate auth backend
AUTHENTICATION_BACKENDS = ("django.contrib.auth.backends.ModelBackend",)
