from django.conf.urls.defaults import *
from views import EpisodeListView, EpisodeDetailView, InstanceTodayArchiveView

urlpatterns = patterns('',
    url(r'^$', EpisodeListView.as_view(), name='home'),
    url(r'^(?P<pk>\d+)/$', EpisodeDetailView.as_view(), name='episode_detail'),
    url(r'^schedule/$', InstanceTodayArchiveView.as_view(), name='schedule_today')
)