SHELL=/bin/sh

HASH   := $(shell git rev-parse HEAD)

er:
	pipenv run python manage.py graph_models main | dot -Tpng > doc/main_allmodels.png
	cp doc/*.png project/apps/main/static/main/img/

.PHONY: init_dev_db
init_dev_db: er
	pipenv run python manage.py makemigrations
	pipenv run python manage.py migrate
	pipenv run python manage.py createsuperuser --email admin@admin.org --username admin

.PHONY: clean
clean:
	@echo Cleaning ...
	@find . -name "__pycache__" -exec rm -rf {} \;
	@find . -name "*.pyc" -exec rm -rf {} \;
	@echo ... done

.PHONY: docker_build
docker_build: er
	docker build \
		--tag sas_api \
		--build-arg HASH=$(HASH) \
		.

.PHONY: docker_test
docker_test: docker_build
	docker run \
		--env "AWS_ACCESS_KEY_ID=$(AWS_ACCESS_KEY_ID)" \
		--env "AWS_SECRET_ACCESS_KEY=$(AWS_SECRET_ACCESS_KEY)" \
		--env "LOGIN_REDIRECT_URL=$(LOGIN_REDIRECT_URL)" \
		--env "SSSC_URL=$(SSSC_URL)" \
		--env "SOCIAL_AUTH_GOOGLE_OAUTH2_KEY=$(SOCIAL_AUTH_GOOGLE_OAUTH2_KEY)" \
		--env "SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET=$(SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET)" \
		--env "GIT_COMMIT_HASH=$(HASH)" \
		sas_api python manage.py test
