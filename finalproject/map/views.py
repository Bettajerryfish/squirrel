from django.shortcuts import render

from .models import Squirrel


def squirrels_map(request):
    sightings=Squirrel.objects.all()[:100]

    return render(request, 'map/squirrel_map.html',{'sightings':sightings})

# Create your views here.
