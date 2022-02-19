from django.contrib.auth import get_user_model
from celery import shared_task, Celery
from django.core.mail import send_mail

PASSWORD = 'shani_1234'
URL = f'redis://:{PASSWORD}@127.0.0.1:6379/0'

# app = Celery('tasks', broker=URL)

@shared_task(bind=True)
def send_mail_func(self):
    users = get_user_model().objects.all()
    for user in users:
        mail_subject = "Hi! Celery Testing"
        message = "this task will send email to all users"
        send_mail(
            mail_subject,
            message,
            'fimbaycare@gmail.com',
            [user.email],
            fail_silently=False,
        )
    return "Done"