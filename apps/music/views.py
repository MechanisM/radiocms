from django.views.generic import DetailView
from models import Artist
from programmes.models import SongSegment


class ArtistDetailView(DetailView):

    model = Artist
    context_object_name = 'artist'
    
    def get_context_data(self, **kwargs):
        context = super(ArtistDetailView, self).get_context_data(**kwargs)
        try:
            context['recent_segments'] = SongSegment.objects.\
                filter(song__artist=self.object).select_related()[:5]
        except:
            pass
        return context
