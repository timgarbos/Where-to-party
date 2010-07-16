from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
(r'^facebook/', include('facebookconnect.urls')),
    
    (r'^places/', include('bringiton.places.urls')),

    (r'^', include('bringiton.home.urls')),

    (r'^admin/doc/', include('django.contrib.admindocs.urls')),


    (r'^admin/', include(admin.site.urls)),

(r'^site_media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': 'http://garbos.itu.dk/bringiton/'}),
)
