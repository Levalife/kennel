from django.db import models
from django.forms import ModelForm, Textarea, TextInput
from captcha.fields import CaptchaField
from django.utils.translation import ugettext_lazy as _
#class Contact(models.Model):

class Contact(models.Model):
	title = models.CharField(_('Message title'), max_length=100)
	name = models.CharField(_('Your name'), max_length=100)
	mail = models.EmailField(_('Your email adress'), max_length=100)
	text = models.TextField(_('Message'))

	class Meta:
		verbose_name = 'Message'
		verbose_name_plural = 'Messages'

	def __unicode__(self):
		return self.title

class ContactForm(ModelForm):
	captcha = CaptchaField(label=_('Confirmation code'))

	class Meta:
		model = Contact
		
