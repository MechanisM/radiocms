from django.conf.urls.defaults import *
from views import ArtistDetailView

urlpatterns = patterns('',
    url(r'^artists/(?P<pk>\d+)/$', ArtistDetailView.as_view(), name='artist_detail'),
)