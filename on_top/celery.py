import os
from celery import Celery
from celery.schedules import crontab
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'on_top.settings')

app = Celery('on_top')
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()
app.conf.beat_schedule = {
    'send-message-every-single-minute': {
        'task': 'dashboard.tasks.send_message',
        'schedule': crontab(),  # change to `crontab(minute=0, hour=0)` if you want it to run daily at midnight
    },
}
