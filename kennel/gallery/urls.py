from django.conf.urls import url, patterns
from views import albums, album

urlpatterns = patterns('',
	url(r'^albums/$', albums, name='albums'),
	url(r'^(?P<album_id>\d+)/(?P<view>full|thumbnails)/$', album, name='album'),

)