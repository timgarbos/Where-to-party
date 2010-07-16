from django.conf.urls.defaults import *
urlpatterns = patterns('bringiton.places.views',
    (r'^places/$', 'index'),
    (r'^places/(?P<place_id>\d+)/$', 'detail'),

)

