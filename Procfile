release: rm -rf db.sqlite3 && python manage.py migrate && python manage.py seed
web: gunicorn TheIndex.wsgi --log-file -
