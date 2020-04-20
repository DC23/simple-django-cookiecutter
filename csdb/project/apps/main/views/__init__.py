# -*- coding: utf-8 -*-

# Ignore unused imports warning
# pylama: ignore=W0611

# You must import all views here
from .index import IndexView
from .er import ErView

# Dev views, remove later
from .debug import DebugView
from .lorem import LoremView
