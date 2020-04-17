# simple-django-cookiecutter

Cookiecutter template for a simple Django 3 website with Bootstrap4 and Docker support.

If you are looking for a modern and stylish Django 3 skeleton project, turn
around and run away. Do not walk. This is not the project you are looking for.

If you are looking for a basic skeleton application with a cliche 4-pane layout
(header, footer, left-hand nav panel and scrolling main content panel), then
maybe this will help.

TODO: add screenshot

The template as generated has just one app that handles all functionality.
I know this is not best-practice so feel free to split into multiple apps if
required.

I wrote this cookiecutter template simply because I don't want to repeat the
same basic setup for small internal projects. If it is useful to someone else
then great, but that is not the primary driver.

## Current Features

* Python 3.6
* Django 3.0
* Bootstrap 4.1.1
* Bootswatch
* Django Debug toolbar (only in development mode)
* Stock Django Admin console
* Main app views and models are directories rather than a single file.
* Functional (but boring) views and templates for the full Django authentication
  workflow.
* [django-split-settings](https://github.com/sobolevn/django-split-settings)
* [python-decouple](https://github.com/henriquebastos/python-decouple)
* A Dockerfile
* My preferred directory layout for projects and apps
* [Bumpversion](https://github.com/peritus/bumpversion)
* Code formatting by [Black](https://github.com/psf/black)
* Linting by [pylama](https://pylama.readthedocs.io/en/latest/)
* django-extensions installed
* Utility Makefile with common commands, including generation of
  Entity-Relationship diagrams.
* Simple view for viewing the latest ER diagrams. This is useful for sharing
  data modelling progress with key users during development.
* A `Pipfile` for working with (pipenv)[https://pipenv.pypa.io/en/latest/]
* Pre-configured `.vscode/launch.json` for running the dev server from VS Code.

More details on the directory layout, and the use of django-split-settings and
python-decouple are in the generated project README.
