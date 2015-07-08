from django.core.urlresolvers import reverse
from django.db import models
from django.db.models.signals import post_save
# Create your models here.



class Gadgets(models.Model):
	CATEGORY_CHOICES = (
    ('0', 'laptops'),
    ('1', 'desktops'),
    ('2', 'tablets'),
	)
	title = models.CharField(max_length=120)
	description = models.TextField(null=True, blank=True)
	category = models.CharField(max_length=1, choices=CATEGORY_CHOICES)
	price = models.FloatField(null=True)
	image = models.ImageField(upload_to='static/media/products/images')

	def __unicode__(self):
		return self.title




+----+-------+--------------+----------+-------+--------------------------+
| id | title | description  | category | price | image                    |
+----+-------+--------------+----------+-------+--------------------------+
|  1 | CAT   | CAT IS BLACK | 0        |   200 | static/images/jinn.gif   |
|  2 | BAT   | BAT IS WHITE | 1        |   100 | static/images/bara.gif   |
|  3 | MAT   | MAT IS PLAIN | 2        |   120 | static/images/zainab.gif |
+----+-------+--------------+----------+-------+--------------------------+

https://github.com/edcrewe/django-csvimport