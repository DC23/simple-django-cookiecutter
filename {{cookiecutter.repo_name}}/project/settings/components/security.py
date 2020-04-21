# -*- coding: utf-8 -*-

# Security
# https://docs.djangoproject.com/en/3.0/topics/security/

SESSION_COOKIE_HTTPONLY = True
CSRF_COOKIE_HTTPONLY = True
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_BROWSER_XSS_FILTER = True
X_FRAME_OPTIONS = "DENY"

CORS_ORIGIN_ALLOW_ALL = True

# Allows setting the draft security HTTP header Feature-Policy on your Django app.
# https://pypi.org/project/django-feature-policy/
FEATURE_POLICY = {}

# Timeouts
EMAIL_TIMEOUT = 5
