from django.conf.urls.defaults import *
from views import EpisodeListView, EpisodeDetailView

urlpatterns = patterns('',
    url(r'^$', EpisodeListView.as_view(), name='home'),
    url(r'^(?P<pk>\d+)/$', EpisodeDetailView.as_view(), name="episode_detail"),
)