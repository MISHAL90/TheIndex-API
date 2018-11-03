release: python manage.py flush --no-input && python manage.py migrate && python manage.py seed
web: gunicorn TheIndex.wsgi --log-file -
