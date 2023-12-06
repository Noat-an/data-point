#!/bin/sh

if [ "$DATABASE" = "postgres" ]
then
    echo "Waiting for postgres..."

    while ! nc -z $SQL_HOST $SQL_PORT; do
      sleep 0.1
    done

    echo "PostgreSQL started"
fi

if [ "$DEBUG" = "1" ]
then
    poetry install
    echo "Creating the database tables..."
    poetry run alembic revision
    poetry run alembic upgrade head
    echo "Tables created"
    poetry run app
    echo "App started"
fi

exec "$@"