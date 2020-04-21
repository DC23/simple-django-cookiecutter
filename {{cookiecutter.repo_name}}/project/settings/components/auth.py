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

# JWT_AUTH = {
# "JWT_ALLOW_REFRESH": True,
# "JWT_EXPIRATION_DELTA": timedelta(minutes=15),
# "JWT_AUTH_HEADER_PREFIX": "JWT",
# }

# SIMPLE_JWT = {
#     "ACCESS_TOKEN_LIFETIME": timedelta(minutes=1),
#     "REFRESH_TOKEN_LIFETIME": timedelta(minutes=2),
#     "ROTATE_REFRESH_TOKENS": False,
#     "BLACKLIST_AFTER_ROTATION": True,
#     "ALGORITHM": "HS256",
#     "SIGNING_KEY": SECRET_KEY,
#     "VERIFYING_KEY": None,
#     "AUTH_HEADER_TYPES": ("JWT",),
#     "USER_ID_FIELD": "id",
#     "USER_ID_CLAIM": "user_id",
#     "AUTH_TOKEN_CLASSES": ("rest_framework_simplejwt.tokens.AccessToken",),
#     "TOKEN_TYPE_CLAIM": "token_type",
#     "SLIDING_TOKEN_REFRESH_EXP_CLAIM": "refresh_exp",
#     "SLIDING_TOKEN_LIFETIME": timedelta(minutes=5),
#     "SLIDING_TOKEN_REFRESH_LIFETIME": timedelta(days=1),
# }
