from django.conf.urls.defaults import *

urlpatterns = patterns('apps.programmes.views',
    url(r'^$', 'home', name='home'),
    url(r'^(\d+)/$', 'programme_detail', name='home'),
)