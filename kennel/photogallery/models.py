from django.db import models

class Album(models.Model):
	title = models.CharField('Album name', max_length=100)
	slug = models.SlugField(max_length=100, unique=True)
	img = models.ImageField(upload_to='media')

	class Meta:
		ordering = ['title']
		verbose_name= 'Album'
		verbose_name_plural = 'Albums'

	def __unicode__(self):
		return self.title

class Photo(models.Model):
	title = models.CharField('Photo name', max_length=100)
	album = models.ForeignKey(Album, verbose_name='Album')
	img = models.ImageField('Photo', upload_to='media')

	class Meta:
		ordering = ['title']
		verbose_name =  'Photo'
		verbose_name_plural = 'photos'

	def __unicode__(self):
		return self.title