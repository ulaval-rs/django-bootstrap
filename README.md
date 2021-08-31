# Bootstrap Django
A simple [Django 3](https://www.djangoproject.com/) project with sane defaults to get you started. Powered by [docker](https://www.docker.com/) and [compose](https://github.com/docker/compose).

## Features
* Configured with [django-rest-framework](https://www.django-rest-framework.org/) and some useful plugins
* Separate configurations for local, dev and prod environments
* [black](https://github.com/psf/black) and [flake8](https://github.com/PyCQA/flake8) formatting and linting
* CI and tests using github actions, [pytest](https://docs.pytest.org/en/6.2.x/) and [factory_boy](https://github.com/FactoryBoy/factory_boy)
* [redis](https://redis.io/) caching in dev
* [postgres](https://www.postgresql.org/) db in dev
* Themed admin using [django-admin-interface](https://github.com/fabiocaccamo/django-admin-interface)


## Usage (simple)
1. `docker compose build` and `docker compose up` to run the project
2. Visit http://localhost:8080/admin/ to login using admin:secret as credentials
3. Connect to the container suing `docker compose exec api bash`
4. Run tests in the container using `pytest`.
5. Create new apps in the container using `python manage.py startapp my_app`
6. Put new apps in backend/apps/ and edit their apps.py file to add `apps.` in front of their app name (ie. `name = "my_app"` becomes `name = "apps.my_app"`)
7. Add new apps to backend/api/settings/base.py, in the `LOCAL_APPS` list (ie. `"apps.my_app",`)
8. Don't forget to delete `db.sqlite3` in the backend/ directory to clear the database.

## Usage (advanced)
1. Edit the DB_PREFIX value in backend/api/settings/base.py to match your project
2. Create a .env file based on the content of .env.dev.example. This will be used when running the development version (docker-compose.dev.yml)
3. Run using `docker compose -f docker-compose.dev.yml build` and `docker compose -f docker-compose.dev.yml up`
4. Visit http://localhost:8080/admin/ to login using the default superadmin user defined in `.env`
5. don't forget to reference fixtures in backend/conftest.py

## Usage (production)
1. Make sure DEBUG=False in backend/api/settings/prod.py
2. Tag and build your image using `docker build -t my_project:my_tag .`
3. Push your image to a registry
4. Add the correct environment variables to your deployment configuration. The most important are:
   1. Database information for obvious reasons
   2. DJANGO_MANAGE_MIGRATE=on for the entrypoint to migrate new changes every deployment
   3. redis information if necessary
5. Do not use any command (ie. dev uses `python manage.py runserver`). See the Dockerfile for commands to use. By default it uses [gunicorn](https://gunicorn.org/), but info for AWS deployments is also available.
