from django.views.generic.list_detail import object_list, object_detail
from models import Show

def home(request):
    return object_list(
        request,
        queryset=Show.objects.all(),
    )

def programme_detail(request):
    pass