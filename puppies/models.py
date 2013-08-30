from django.db import models

import datetime

from gallery.models import Album

class Puppies(models.Model):
	litter = models.CharField(max_length=15)
	mother = models.CharField(max_length=100)
	mother_photo = models.ImageField(upload_to='media', blank=True)
	mother_pedigree = models.URLField(max_length=100, blank=True)
	mother_health = models.CharField(max_length=200, blank=True)
	mother_titles = models.CharField(max_length=100, blank=True)
	mother_training = models.CharField(max_length=100, blank=True)
	father = models.CharField(max_length=100)
	father_photo = models.ImageField(upload_to='media', blank=True)
	father_pedigree = models.URLField(max_length=100, blank=True)
	father_health = models.CharField(max_length=100, blank=True)
	father_titles = models.CharField(max_length=200, blank=True)
	father_training = models.CharField(max_length=100, blank=True)
	birthday = models.DateField(blank=True)
	amount = models.CharField(max_length=40, blank=True)
	gallery = models.ForeignKey(Album, blank=True, null=True)

	class Meta():
		verbose_name_plural = 'Puppies'

	def __unicode__(self):
		return self.litter
