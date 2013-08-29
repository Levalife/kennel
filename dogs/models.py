from django.db import models
import datetime

from gallery.models import Album

class Gender(models.Model):
	gender = models.CharField(max_length=15)

	def __unicode__(self):
		return self.gender

class Dog(models.Model):
	name = models.CharField(max_length=80, blank=True)
	mother = models.CharField(max_length=80, blank=True)
	father = models.CharField(max_length=80, blank=True)
	breeder = models.CharField(max_length=80, blank=True)
	photo = models.ImageField(upload_to='media', blank=True)
	sex = models.ForeignKey(Gender)
	birthday = models.DateField()
	pedigree = models.URLField(max_length=150, blank=True)
	hd = models.CharField(max_length = 40, blank=True) 
	mdr1 = models.CharField(max_length = 40, blank=True)
	dm = models.CharField(max_length=40, blank=True)
	titles = models.TextField(max_length=400, blank=True)
	training = models.CharField(max_length=80, blank=True)
	about_dog = models.TextField(max_length=400, blank=True)
	gallery = models.ForeignKey(Album, blank=True, null=True)

	def __unicode__(self):
		return self.name