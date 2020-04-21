# -*- coding: utf-8 -*-

# Caching
# TODO: enable caching?
# https://docs.djangoproject.com/en/3.0/topics/cache/

CACHES = {
    "default": {"BACKEND": "django.core.cache.backends.locmem.LocMemCache"},
    # 'axes_cache': {
    #     'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
    # },
}


# TODO: enable django-axes?
# django-axes
# https://django-axes.readthedocs.io/en/latest/configuration.html
# See #known-configuration-problems section

# AXES_CACHE = 'axes_cache'
