from celery import shared_task, Celery
from djangoWithCelery.settings import broker_url,result_backend

PASSWORD = 'shani_1234'
URL = f'redis://:{PASSWORD}@127.0.0.1:6379/0'

app = Celery('djangoWithCelery', backend=result_backend, broker=broker_url)
# app = Celery('tasks', broker=URL)

@shared_task(bind=True)
def test_func(self):
    for i in range(19):
        print(i)
    return "Success"

@app.task
def add():
    res = 4+5
    print(res)
    return res