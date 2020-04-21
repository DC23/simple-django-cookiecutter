# -*- coding: utf-8 -*-

"""
This is a django-split-settings main file.

For more information read this:
https://github.com/sobolevn/django-split-settings

To change settings file:
`DJANGO_ENV=production python manage.py runserver`
"""

from pathlib import PurePath
from decouple import AutoConfig
from split_settings.tools import include, optional

# Build the root project directory
BASE_DIR = PurePath(__file__).parents[2]

# Loading environment variables from actual variables or `.env` files
# with better typesafety than os.environ.
# See https://github.com/henriquebastos/python-decouple
config = AutoConfig(search_path=BASE_DIR.joinpath("config"))

# Production or Development?
ENV = config("DJANGO_ENV", default="development")

settings = [
    "components/common.py",
    "components/auth.py",
    "components/bootstrap.py",
    "components/caches.py",
    "components/csp.py",
    "components/database.py",
    "components/email.py",
    "components/logging.py",
    "components/security.py",
    "components/settings_export.py",
    # Select the right environment:
    f"environments/{ENV}.py",
    # Optional local overrides:
    optional("environments/local.py"),
]

# Parse and include all settings:
include(*settings)
