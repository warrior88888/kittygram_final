FROM python:3.10-slim AS builder
WORKDIR /app
COPY backend/requirements.txt .
RUN pip install --no-cache-dir --prefix=/install -r requirements.txt

FROM python:3.10-slim
WORKDIR /app

COPY --from=builder /install /usr/local
COPY . .

RUN apt-get update && apt-get install -y netcat-openbsd && rm -rf /var/lib/apt/lists/*

CMD ["sh", "-c", "while ! nc -z db 5432; do sleep 1; done && python manage.py migrate && python manage.py collectstatic --no-input && gunicorn --bind 0.0.0.0:8000 kittygram_backend.wsgi"]