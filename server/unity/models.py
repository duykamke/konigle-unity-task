from django.db import models
from django.utils.translation import gettext_lazy as _

class User(models.Model):

    SUBSCRIPTION_CHOICES = [
        (1, 'Subscribed'),
        (0, 'Unsubscribed'),
    ]

    email = models.CharField(max_length=100, primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    subscription_status = models.IntegerField(
        choices=SUBSCRIPTION_CHOICES,
        default=1,
    )

def __str__(self):
    return self.email
