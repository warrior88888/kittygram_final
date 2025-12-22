FROM python:3.10-slim AS builder

WORKDIR /app

COPY backend/requirements.txt ./backend/requirements.txt
RUN pip install --no-cache-dir --prefix=/install -r ./backend/requirements.txt


FROM python:3.10-slim

WORKDIR /app

COPY --from=builder /install /usr/local

COPY tests.yml ./tests.yml
COPY docker-compose.production.yml ./docker-compose.production.yml
COPY kittygram_workflow.yml ./kittygram_workflow.yml
COPY pytest.ini ./pytest.ini

COPY backend ./backend

RUN apt-get update && apt-get install -y netcat-openbsd && rm -rf /var/lib/apt/lists/*

CMD ["sh", "-c", "while ! nc -z db 5432; do sleep 1; done && python /app/backend/manage.py migrate && python /app/backend/manage.py collectstatic --no-input && gunicorn --chdir /app/backend --bind 0.0.0.0:8000 kittygram_backend.wsgi"]
