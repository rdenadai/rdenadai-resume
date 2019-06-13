web: python manage.py migrate --noinput && python manage.py compress --force && python manage.py collectstatic --no-input; gunicorn resume.wsgi --workers=3 --reload
