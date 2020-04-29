# -*- coding: utf-8 -*-

# django-bootstrap4 settings
# See: https://django-bootstrap4.readthedocs.io/en/latest/index.html

bootstrap_version = "4.1.1"

# See https://bootswatch.com/ for theme names
# bootstrap_theme = "yeti"
# bootstrap_theme = "flatly"
# bootstrap_theme = "sandstone"
# bootstrap_theme = "cerulean"
# bootstrap_theme = "simplex"
# bootstrap_theme = "spacelab"

BOOTSTRAP4 = {
    "css_url": {
        "href": f"https://stackpath.bootstrapcdn.com/bootstrap/{bootstrap_version}/css/bootstrap.min.css",
        "integrity": "sha384-WskhaSGFgHYWDcbwN70/dfYBj47jz9qbsMId/iRN3ewGhXQFZCSftd1LZCfmhktB",
        "crossorigin": "anonymous",
    },
    "javascript_url": {
        "url": f"https://stackpath.bootstrapcdn.com/bootstrap/{bootstrap_version}/js/bootstrap.min.js",
        "integrity": "sha384-smHYKdLADwkXOn1EmN1qk/HfnUcbVRZyYmZ4qpPea6sjB/pTJ0euyQp0Mk8ck+5T",
        "crossorigin": "anonymous",
    },
}

try:
    BOOTSTRAP4["theme_url"] = {
        "url": f"https://stackpath.bootstrapcdn.com/bootswatch/{bootstrap_version}/{bootstrap_theme}/bootstrap.min.css",
        "crossorigin": "anonymous",
    }
except NameError:
    pass  # Ignore this error if no theme is defined
