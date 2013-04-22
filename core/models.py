from django.db import models
from inventory import settings
from auth.models import User

# Create your models here.
class Collection(models.Model):
	name = models.CharField(max_length=200)
	added = models.DateField(auto_now=True)
	user = models.ForeignKey(User)

	def __str__(self):
		return self.name

class Item(models.Model):
	name = models.CharField(max_length=200)
	collection = models.ManyToManyField(Collection)
	added = models.DateField(auto_now=True)
	user = models.ForeignKey(User)


class File(models.Model):
	nicename = models.CharField(max_length=200)
	file = models.FileField(max_length=200, upload_to=settings.MEDIA_ROOT)
	item = models.ForeignKey(Item)
	user = models.ForeignKey(User)
	temporarysession = models.CharField(max_length=200, blank=True)
	


	


