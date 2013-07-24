from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()



from django.conf.urls import *
from django.conf import settings

from views import home
from contacts.views import ContactCreateView
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'kennel.views.home', name='home'),
    # url(r'^kennel/', include('kennel.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', home, name='home'),
    #url(r'^gallery/', include('photogallery.urls', namespace='photogallery')),
    url(r'^dogs/', include('dogs.urls', namespace='dogs')),
    url(r'^puppies/', include('puppies.urls', namespace='puppies')),
    url(r'^offsprings/', include('offsprings.urls', namespace='offsprings')),
    url(r'^history/$', TemplateView.as_view(template_name='history.html'), name='history'),
    url(r'^standard/$', TemplateView.as_view(template_name='standard.html'), name='standard'),
    url(r'^whythisbreed/$', TemplateView.as_view(template_name='whythisbreed.html'), name='whythisbreed'),
    url(r'^contacts/$', ContactCreateView.as_view(), name='contacts'),
    url(r'^thanks/$', TemplateView.as_view(template_name='success_contact.html')),
    url(r'^gallery/', include('gallery.urls', namespace='gallery'))
)

#for media
urlpatterns += patterns('',
 url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
)

#for captcha 
urlpatterns += patterns('',
    url(r'^captcha/', include('captcha.urls')),
)


