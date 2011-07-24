from django.views.generic import DetailView, ListView, TodayArchiveView
from models import Episode, Instance


class EpisodeListView(ListView):

    model = Episode
    context_object_name = 'episode_list'


class EpisodeDetailView(DetailView):

    model = Episode
    context_object_name = 'episode'


class InstanceTodayArchiveView(TodayArchiveView):

    model = Instance
    context_object_name = 'todays_instances_list'
    date_field = 'tx_time'
