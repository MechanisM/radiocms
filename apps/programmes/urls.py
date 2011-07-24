from django.conf.urls.defaults import *

urlpatterns = patterns('apps.programmes.views',
    url(r'^$', 'home', name='home'),
    url(r'^(\d+)/$', 'episode_detail', name='episode_detail'),
)