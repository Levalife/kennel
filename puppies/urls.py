from django.conf.urls import patterns, url
from views import puppies, litter

urlpatterns = patterns('',
	url(r'^$', puppies, name='our_puppies'),
	url(r'^(?P<puppies_id>\d+)/$', litter, name='litter'),
)