from django.db import models

import datetime

from dogs.models import Gender
from photogallery.models import Album

class Offspring(models.Model):
	name = models.CharField(max_length=80)
	mother = models.CharField(max_length=80)
	father = models.CharField(max_length=80)
	owner = models.CharField(max_length=80, blank=True)
	city = models.CharField(max_length=80, blank=True)
	photo = models.ImageField(upload_to='media', blank=True)
	sex = models.ForeignKey(Gender)
	birthday = models.DateField()
	pedigree = models.URLField(max_length=150, blank=True)
	hd = models.CharField('HD', max_length = 40, blank=True) 
	mdr1 = models.CharField('MDR1', max_length = 40, blank=True)
	dm = models.CharField('DM', max_length=40, blank=True)
	titles = models.TextField(blank=True)
	training = models.CharField(max_length=80, blank=True)
	about_dog = models.TextField(blank=True)
	gallery = models.ForeignKey(Album)

	def __unicode__(self):
		return self.name

