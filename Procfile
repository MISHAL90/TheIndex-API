release: python manage.py migrate && python manage.py seed
web: gunicorn TheIndex.wsgi --log-file -
