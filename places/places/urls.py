from django.urls import path
from django.conf.urls import include
from django.views.decorators.csrf import csrf_exempt

from . import views

urlpatterns = [
    path('places/', views.PlaceList),
    path('placecreate/', csrf_exempt(views.PlaceCreate), name='placeCreate'),
    path('createplaces/', csrf_exempt(views.PlacesCreate), name='createPlaces'),
]