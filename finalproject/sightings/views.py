from django.shortcuts import render

from django.http import HttpResponse,HttpResponseRedirect
from map.models import Squirrel
from .forms import SquirrelForm
# Create your views here.
def sighting (request):
    sightings=Squirrel.objects.all()
    context={'sightings':sightings,} 
    return render(request,"sightings/sighting.html",context)

def stats(request):
    sq_all=Squirrel.objects.all().count()
    Run=Squirrel.objects.filter(Running=True).count()
    Chase=Squirrel.objects.filter(Chasing=True).count()
    Climb=Squirrel.objects.filter(Climbing=True).count()
    Eat=Squirrel.objects.filter(Eating=True).count()
    context={'Run':Run,'Chase':Chase,'Climb':Climb,'Eat':Eat,'sq_all':sq_all,}
    return render(request,'sightings/stats.html',context)

def add(request):
    if request.method=="POST":
        form=SquirrelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('sightings:sighting')
    else:
        form=SquirrelForm()

    context={'form':form}
    return render(request,'sightings/add.html',context)


def update(request, Unique_Squirrel_ID):
    sighting = squirrels.objects.get(Unique_Squirrel_ID=Unique_Squirrel_ID)
    if request.method=="POST":
        form=SquirrelForm(request.POST,instance=sighting)
        if form.is_valid()
            form.save()
            return redirect('sightings:sighting')
    else:
        form=SquirrelForm(instance=sighting)
    context={'form':form, 'Unique_Squirrel_ID' = Unique_Squirrel_ID}
    return render(request,'sightings/update.html',context)

# Create your views here.
