import datetime

from celery import shared_task
from .models import User
from django.core.mail import send_mail

@shared_task
def send_email_periodically():
    today = datetime.date.today()
    first = today.replace(day=1)
    last_month = first - datetime.timedelta(days=1)

    count_all = User.objects.count()
    count_monthly = User.objects.filter(created_at__gte=(last_month)).count()
    count_unsubscribed = User.objects.filter(subscription_status=0).count()

    ### WILL HAVE TO SETUP SMTP SERVER AND PUT EMAIL ON LOWER SECURITY MODE. FOR THE SAKE OF THE TEST, I WILL JUST PRINT THE RESULT
    # send_mail(
    #     'User Information',
    #     'Content',
    #     'from@example.com',
    #     ['to@example.com'],
    #     fail_silently=False,
    # )

    print(count_all, count_monthly, count_unsubscribed)