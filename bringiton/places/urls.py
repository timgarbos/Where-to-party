from django.conf.urls.defaults import *
urlpatterns = patterns('bringiton.places.views',
    (r'^$', 'index'),
    (r'^(?P<place_id>\d+)/$', 'detail'),

)

