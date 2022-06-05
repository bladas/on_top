web: python manage.py runserver 0.0.0.0:$PORT
worker: celery -A on_top worker -events -loglevel info
beat: celery -A on_top beat