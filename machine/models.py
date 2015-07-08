from django.core.urlresolvers import reverse
from django.db import models
from django.db.models.signals import post_save
# Create your models here.


class Gadgets(models.Model):
	title = models.CharField(max_length=120)
	description = models.TextField(null=True, blank=True)
	category = models.CharField(max_length=100)
	price = models.FloatField(null=True)
	image = models.ImageField(upload_to='media/pictures/')

	def __unicode__(self):
		return self.title