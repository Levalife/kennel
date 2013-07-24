from django.conf.urls import url, patterns

from views import news_page

urlpatterns = patterns('',
	url(r'^(?P<news_id>\d+)/$', news_page, name='news_page'),
)