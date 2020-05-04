SHELL=/bin/sh

HASH   := $(shell git rev-parse HEAD)

.PHONY: clean
clean:
	@echo Cleaning ...
	@find . -name "__pycache__" -exec rm -rf {} \;
	@find . -name "*.pyc" -exec rm -rf {} \;
	@echo ... done

er:
	pipenv run python manage.py graph_models main | dot -Tpng > doc/main_allmodels.png
	cp doc/*.png project/apps/main/static/main/img/

.PHONY: init_dev_db
init_dev_db: er
	pipenv run python manage.py makemigrations
	pipenv run python manage.py migrate
	pipenv run python manage.py createsuperuser --email admin@admin.org --username admin

.PHONY: docker_build
docker_build: er
	docker build \
		--tag {{ cookiecutter.docker_image_name }}/{{ cookiecutter.version }} \
		--build-arg HASH=$(HASH) \
		.

.PHONY: docker_test
docker_test: docker_build
	docker run \
		--env "GIT_COMMIT_HASH=$(HASH)" \
		{{ cookiecutter.docker_image_name }} python manage.py test
