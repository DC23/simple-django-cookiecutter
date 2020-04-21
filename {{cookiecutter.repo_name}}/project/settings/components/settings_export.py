# -*- coding: utf-8 -*-

# Settings_Export: control which project settings are exposed to templates
# See: https://github.com/jakubroztocil/django-settings-export

SETTINGS_EXPORT = [
    "SITE_NAME",
    "DEBUG",
    "ENV",
]

# Settings can be accessed in templates via `{{ settings.<KEY> }}`.
