from django.db import models
from django.conf import settings
from allauth.account.signals import user_logged_in, user_signed_up
# Create your models here.

class profile(models.Model):
    name = models.CharField(max_length=120)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, null= True, blank=True)
    description = models.TextField(default='desciption default text')

    def __unicode__(self):
        return self.name

class userStripe(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    stripe_id = models.CharField(max_length=200, null=True, blank=True)

    def __unicode__(self):
        if self.stripe_id:
            return str(self.stripe_id)
        else:
            return self.user.username
