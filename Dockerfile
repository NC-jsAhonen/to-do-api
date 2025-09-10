FROM python:3.11-slim
WORKDIR /app

# Prevent .pyc files and buffer stdout
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# Install system deps (for psycopg2, if using Postgres)
RUN apt-get update && \
    apt-get install -y build-essential libpq-dev && \
    apt-get clean

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
WORKDIR /app/todo_api

# Collect static files if you use them
# RUN python manage.py collectstatic --noinput

CMD ["gunicorn", "todo_api.wsgi:application", "--bind", "0.0.0.0:8000"]