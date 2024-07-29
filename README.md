# Fancy Music Library Project

A sample Django Rest Framework app with Celery integration.

## API
`FML API` app is used for storing and managing music library data. It provides endpoints for CRUD operations on the following resources and operations:
* Artists
* Albums
* Songs
* Playlists
* \*Admin operations

*requires API key provided in Auth header.

## Celery
Celery is used for asynchronous and periodic tasks. In the context of the application it is used for:
* creating a csv dump of the database every 24 hours.

Any new periodic tasks should be added to `CELERY_BEAT_SCHEDULE` in `FancyMusicLibrary/settings.py`.

## Installation notes
Prerequisites:
* OS: macOS or linux (preferred)
* Redis (follow instructions at https://redis.io/topics/quickstart)
* PostgreSQL (follow instructions at https://www.postgresql.org/download/)
* Python 3.11 with a venv created for this project

To install the dependencies, run:
`pip install -r requirements/all.for.dev.txt`.

## Development
#### Running locally – terminal

1. Run the redis server.
2. Fill `.env` file with the necessary environment variables (including secrets).
3. Export `PYTHONPATH` env var so that it includes path to the `src` dir.
4. Apply migrations to your PostgreSQL database running locally: `python manage.py migrate`.
5. To run the API: run `python manage.py runserver`.
6. To run the Celery beat: run `celery -A FancyMusicLibrary beat --loglevel=info`.
7. To run the Celery worker: run `celery -A FancyMusicLibrary worker --loglevel=info`.

#### Running locally – Docker
Make sure `docker` and `docker-compose` are installed on your machine.
Docker-compose utilizes nginx server to serve the API.

1. Inside `docker` folder run `docker-compose up --build`.
2. Run `docker-compose exec web python manage.py migrate` to apply migrations to locally running PostgreSQL db.

### Pre-commit hooks
Install pre-commit by running:
* `pip install -r requirements/all.for.dev.txt`.
* `pre-commit install`.

To apply hooks to pre-commit changes run: `pre-commit run --all-files`.


## Testing

Packages used:
* pytest (runner)
* pytest-django (Django integration)
* pytest-mock (mocking/patching)

Make sure redis-server is running locally.
Run tests with `pytest` in the `src` directory.
