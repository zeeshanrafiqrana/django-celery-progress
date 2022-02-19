from django.http import HttpResponse
from django.shortcuts import render
from .tasks import test_func, add
from sendEmailApp.tasks import send_mail_func
# Create your views here.

def index(request):
    val = test_func.delay()
    result = add.delay()
    print(result.ready())
    # print(result.get(timeout=1))
    return HttpResponse("Successfully Run")

def send_email_to_all_users(request):
    send_mail_func.delay()
    return HttpResponse("Successfully Send email to all users")