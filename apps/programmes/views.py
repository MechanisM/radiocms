from django.views.generic import DetailView, ListView
from models import Episode


class EpisodeListView(ListView):

    model = Episode
    context_object_name = 'episode_list'


class EpisodeDetailView(DetailView):

    model = Episode
    context_object_name = 'episode'
