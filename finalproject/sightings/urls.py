from django.urls import path
from django.conf.urls import url, include
from . import views

app_name='sightings'

urlpatterns = [

            path('sightings/', views.sighting, name = 'sightings'),
            path('home/', views.home, name = 'home'),
            path('map/', views.map, name = 'map'),
            path('add/', views.add, name = 'add'),
            path('stats/', views.stats, name = 'stats'),
            path('<str:unique_squirrel_id>/', views.edit, name = 'edit'),
            path('<str:unique_squirrel_id>/delete/', views.delete, name = 'delete'),

             ]