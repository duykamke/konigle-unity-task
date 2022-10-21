import os

from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'server.settings')

app = Celery('server')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()

app.conf.beat_schedule = {
    'send-email': {
        'task': 'unity.tasks.send_email_periodically',
        'schedule': crontab(hour=9, day_of_week='mon,wed')
    },
}