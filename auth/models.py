from django.db import models
from django.contrib.auth.models import AbstractUser

class BannedIP(models.Model):
	ip = models.IPAddressField(max_length=20)
	added = models.DateTimeField(auto_now=True)


class FailedLogin(models.Model):
	ip = models.IPAddressField(max_length=20)
	added = models.DateTimeField(auto_now=True)


##################
class User(AbstractUser):
	api_key = models.CharField(max_length=100)
##################