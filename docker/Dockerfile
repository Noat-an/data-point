FROM python:3.10-slim

WORKDIR /app/

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install system dependencies
RUN apt-get update \
    && apt-get upgrade -y \
    && apt-get install -y gcc python3-dev libpq-dev netcat-traditional

# install dependencies
RUN pip install poetry==1.6.1
ENV POETRY_VIRTUALENVS_IN_PROJECT=true

COPY ./poetry.lock ./pyproject.toml ./
RUN poetry install --no-root --no-cache --no-interaction

COPY ./entrypoint.sh ./alembic.ini ./README.md ./
COPY ./src ./src

# Run flake8
# RUN flake8

#ENTRYPOINT python -m src.cli.app
ENTRYPOINT ["sh", "/app/entrypoint.sh"]