# -*- coding: utf-8 -*-

from project.settings import BASE_DIR

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR.joinpath("db.sqlite3").as_posix(),
    }
}
