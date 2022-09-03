#!/bin/bash

cd /code
python ./manage.py compress --force
python ./manage.py collectstatic --no-input

if [ "$MIGRATE" = "yes" ]; then
    python ./manage.py makemigrations
    python ./manage.py migrate
fi

if [ "$MODE" = "development" ]; then
    pip install debugpy -t /tmp && python /tmp/debugpy --wait-for-client --listen 0.0.0.0:5678 -m manage runserver 0.0.0.0:8080
elif [ "$MODE" = "production" ]; then
    gunicorn resume.wsgi -b 0.0.0.0:8080 -w 4 --access-logfile - --error-logfile -
fi
