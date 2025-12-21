# Образ должен содержать структуру репозитория в /app, т.к. тесты Практикума
# ищут файлы по путям вида /app/tests.yml и /app/backend/Dockerfile.

FROM python:3.10-slim AS builder

WORKDIR /app

# Устанавливаем зависимости backend (файл лежит в backend/requirements.txt
# относительно корня репозитория).
COPY backend/requirements.txt ./backend/requirements.txt
RUN pip install --no-cache-dir --prefix=/install -r ./backend/requirements.txt


FROM python:3.10-slim

WORKDIR /app

COPY --from=builder /install /usr/local

# Копируем нужные корневые файлы (их требуют тесты).
COPY tests.yml ./tests.yml
COPY docker-compose.production.yml ./docker-compose.production.yml
COPY kittygram_workflow.yml ./kittygram_workflow.yml
COPY pytest.ini ./pytest.ini

# Копируем backend как папку /app/backend
COPY backend ./backend

# netcat нужен для ожидания БД
RUN apt-get update && apt-get install -y netcat-openbsd && rm -rf /var/lib/apt/lists/*

# Запускаем Django из /app/backend
CMD ["sh", "-c", "while ! nc -z db 5432; do sleep 1; done && python /app/backend/manage.py migrate && python /app/backend/manage.py collectstatic --no-input && gunicorn --chdir /app/backend --bind 0.0.0.0:8000 kittygram_backend.wsgi"]
