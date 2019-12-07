from django.shortcuts import render,get_object_or_404

from django.http import HttpResponse,HttpResponseRedirect
from map.models import Squirrel
from .forms import SquirrelForm
# Create your views here.
def index (request):
    sightings=Squirrel.objects.all()
    context={'sightings':sightings,} 
    return render(request,"sightings/index.html",context)

def stats(request):
    Total_Num=Squirrel.objects.all().count()
    Run=Squirrel.objects.filter(running=True).count()
    Chase=Squirrel.objects.filter(chasing=True).count()
    Climb=Squirrel.objects.filter(climbing=True).count()
    Eat=Squirrel.objects.filter(eating=True).count()
    context={'Run':Run,'Chase':Chase,'Climb':Climb,'Eat':Eat,'Total_Num':Total_Num,}
    return render(request,'sightings/stats.html',context)

def add(request):
    if request.method=="POST":
        form=SquirrelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('sightings:index')
    else:
        form=SquirrelForm()

    context={'form':form}
    return render(request,'sightings/add.html',context)


#def update(request, unique_squirrel_id):
 #   sighting = get_object_or_404(Squirrel,unique_squirrel_id=unique_squirrel_id)
  #  if request.method=="POST":
   #     form=SquirrelForm(request.POST,instance=sighting)
    #    if form.is_valid():
     #       form.save()
      #      return redirect('sightings:index')
 #   else:
  #      form=SquirrelForm(instance=sighting)
  #  context={'form':form}
   # return render(request,'sightings/update.html',context)
def update(request, unique_squirrel_id):
    edit_sighting = get_object_or_404(Squirrel, unique_squirrel_id=unique_squirrel_id)
    if request.method == "POST":
        form = SquirrelForm(request.POST, instance=edit_sighting)
        if form.is_valid():
            form.save()
            return redirect("/sightings/")
    form = SquirrelForm(instance=edit_sighting)
    return render(request, "sightings/update.html", {"form": form, "unique_squirrel_id":unique_squirrel_id})
# Create your views here.
