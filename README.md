# Bootstrap Django
![CI](https://github.com/ulaval-rs/django-bootstrap/actions/workflows/CI.yaml/badge.svg)

A simple [Django 4](https://www.djangoproject.com/) project with sane defaults to get you started. Powered by [docker](https://www.docker.com/) and [compose](https://github.com/docker/compose).

## Features
* Configured with [django-rest-framework](https://www.django-rest-framework.org/) and some useful plugins
* Separate configurations for local, dev and prod environments
* [black](https://github.com/psf/black) and [flake8](https://github.com/PyCQA/flake8) formatting and linting
* CI and tests using github actions, [pytest](https://docs.pytest.org/en/6.2.x/) and [factory_boy](https://github.com/FactoryBoy/factory_boy)
* [redis](https://redis.io/) caching in dev
* [postgres](https://www.postgresql.org/) db in dev


## Usage (simple)
1. `docker compose build` and `docker compose up` to run the project
2. Visit http://localhost:8080/admin/ to login using admin:secret as credentials
3. Visit http://localhost:8080/api/v1/schema/swagger-ui for an auto-generated api documentation
4. Connect to the container using `docker compose exec api bash`
5. Run tests in the container using `pytest`.
6. Create new apps in the container using `python manage.py startapp my_app`, then put in `apps` folder, and change the name in the app's `apps.py` from `my_app` to `apps.my_app`
7. Add new apps to config/settings/base.py, in the `LOCAL_APPS` list (ie. `"apps.my_app",`)

## Usage (advanced)
1. Edit the DB_PREFIX value in config/settings/base.py to match your project
2. To test with sensible credential information, create a `.env`, which is ignored in the .gitignroe file, and add it to the docker compose files as necessary.
3. Run using `docker compose -f docker-compose.dev.yml build` and `docker compose -f docker-compose.dev.yml up`
4. don't forget to reference test fixtures in conftest.py for pytest
