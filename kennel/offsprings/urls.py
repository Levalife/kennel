from django.conf.urls import url, patterns

from views import offsprings, offspring_page

urlpatterns = patterns('',
	url(r'^$', offsprings, name ='our_offsprings'),
	url(r'^(?P<offspring_id>\d+)/$', offspring_page, name = 'offspring_page'),

)