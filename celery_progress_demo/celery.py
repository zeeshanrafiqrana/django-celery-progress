from __future__ import absolute_import, unicode_literals
# Django settings
import os
from django.conf import settings
# Celery app
from celery import Celery

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'celery_progress_demo.settings')
REDIS_PASSWORD = 'shani_1234'
usrll = f'redis://:{REDIS_PASSWORD}@127.0.0.1:6379/0'

app = Celery('celery_progress_demo', broker=usrll)

# namespace='CELERY' means all celery-related configuration keys
# should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()
