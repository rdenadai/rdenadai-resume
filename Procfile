web: python ./manage.py compress --force && python ./manage.py collectstatic --no-input; gunicorn resume.wsgi --workers=3 --access-logfile gunicorn_access.log --error-logfile gunicorn_error.log
