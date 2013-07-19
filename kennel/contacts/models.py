from django.db import models
from django.forms import ModelForm, Textarea, TextInput
from captcha.fields import CaptchaField
#class Contact(models.Model):

class Contact(models.Model):
	title = models.CharField(max_length=100)
	name = models.CharField(max_length=100)
	mail = models.EmailField(max_length=100)
	text = models.TextField('Message:')

	class Meta:
		verbose_name = 'Message'
		verbose_name_plural = 'Messages'

	def __unicode__(self):
		return self.title

class ContactForm(ModelForm):
	captcha = CaptchaField(label='Confirmation code')

	class Meta:
		model = Contact
