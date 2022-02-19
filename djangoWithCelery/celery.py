from __future__ import absolute_import, unicode_literals
import os

from celery import Celery
from django.conf import settings
from djangoWithCelery.settings import broker_url,result_backend

password = 'shani_1234'
usrll = f'redis://:{password}@127.0.0.1:6379/0'
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangoWithCelery.settings')
app = Celery('djangoWithCelery', backend=result_backend, broker=broker_url)
# app.conf.result_backend
# app.conf.broker_url
app.conf.enable_utc = False
app.conf.update(timezone = 'Asia/Karachi')

app.config_from_object(settings, namespace='CELERY')

# CELERY BEAT SETTINGS
app.conf.beat_schedule = {

}
#
app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print(f'Request:{self.request!r}')
