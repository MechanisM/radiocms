from django.views.generic.list_detail import object_list, object_detail
from models import Episode

def home(request):
    return object_list(
        request,
        queryset=Episode.objects.all(),
    )

def episode_detail(request, object_id):
    return object_detail(
        request,
        queryset=Episode.objects.all(),
        object_id=object_id,
    )