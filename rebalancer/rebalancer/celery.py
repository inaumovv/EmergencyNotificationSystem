import os

from celery import Celery
from celery.app.base import App
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'rebalancer.settings')

app: App = Celery('rebalancer')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

app.conf.beat_schedule = {
    'check-worker-every-5-minutes': {
        'task': 'check_app.tasks.request_to_worker',
        'schedule': crontab(minute='*/5')
    }

}