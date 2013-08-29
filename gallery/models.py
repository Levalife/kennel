from django.db import models
import os
from os.path import join

class Album(models.Model):
	title = models.CharField(max_length=60)
	public = models.BooleanField(default=True)
	def __unicode__(self):
		return self.title

	def images(self):
		lst = [x.image.name for x in self.image_set.all()]
		lst = ["""<a href='/media/%s'>%s</a>""" % (x, x.split('/')[-1]) for x in lst]
		return lst
	images.allow_tags = True

class Image(models.Model):
	title = models.CharField(max_length=60, blank=True, null=True)
	image = models.ImageField(upload_to='media/')
	album = models.ForeignKey(Album, blank=True, null=True)
	created = models.DateTimeField(auto_now_add=True)
	width = models.IntegerField(blank=True, null=True)
	height = models.IntegerField(blank=True, null=True)

	def __unicode__(self):
		return self.image.name

	def size(self):
		return "%s x %s" %(self.width, self.height)

	def thumbnail(self):
		return """<a href="/media/%s"><img border="0" alt="" src="/media/%s" height="40" /></a>""" % (
                                                                    (self.image.name, self.image.name))

	thumbnail.allow_tags = True