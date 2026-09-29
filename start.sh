#!/usr/bin/env bash
set -e

python manage.py migrate --noinput
python manage.py collectstatic --noinput

python manage.py createsuperuser --noinput || true

exec gunicorn resume_website.wsgi:application \
    --bind 0.0.0.0:8000 \
    --workers 1 \
    --timeout 60