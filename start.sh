#!/usr/bin/env bash
set -e

python manage.py migrate --noinput

exec gunicorn resume_website.wsgi:application \
    --bind 0.0.0.0:8000 \
    --workers 2 \
    --timeout 60