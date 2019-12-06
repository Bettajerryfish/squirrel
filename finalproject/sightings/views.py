from django.shortcuts import render

from django.http import HttpResponse,HttpResponseRedirect
from map.models import squirrels
from .forms import SquirrelForm
# Create your views here.
def sighting (request):
        sightings=squirrels.objects.all()
            context={'sightings':sightings,} 
                return render(request,"sightings/sighting.html",context)
# Create your views here.
