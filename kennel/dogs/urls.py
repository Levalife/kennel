from django.conf.urls import patterns, include, url
from views import *

urlpatterns = patterns('',
	url(r'^$', our_dogs, name='our_dogs'),
	url(r'^males/$', males, name='males'),
	url(r'^females/$', females, name='females'),
	url(r'^(?P<dog_id>\d+)/$', dog_page, name='dog_page')

)