from django.conf.urls.defaults import *
from django.views.generic import DetailView
from models import Artist, Song

urlpatterns = patterns('',
    url(r'^artists/(?P<pk>\d+)/$', DetailView.as_view(model=Artist), name='artist_detail'),
)