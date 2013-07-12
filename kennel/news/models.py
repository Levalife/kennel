from django.db import models


import datetime

class News(models.Model):
	title = models.CharField(max_length=200)
	photo = models.ImageField(upload_to="media", help_text='150x150')
	body = models.CharField(max_length=5000)
	pub_date = models.DateTimeField(default = datetime.datetime.now())

	def __unicode__(self):
		return self.title
