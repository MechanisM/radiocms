from django.conf.urls.defaults import *
from django.views.generic import DetailView, ListView
from models import Episode

urlpatterns = patterns('',
    url(r'^$', ListView.as_view(model=Episode), name='home'),
    url(r'^(?P<pk>\d+)/$', DetailView.as_view(model=Episode), name="episode_detail"),
)