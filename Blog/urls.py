from .views import *
from django.urls import path
from . import views



urlpatterns = [
    path('', Main , name='Main'),
    path('Cities/<int:cities_id>/', views.CityTemp, name='CityTemp'),
    path("Cities/pk", CitiesPage, name="Cities"),
   # path("Cities", CitiesPage, name="Cities"),
    path("CityTemp", CityTemp, name="CityTemp"),
    path("Learn", Learn, name="Learn"),
    path("TravelOrders", TravelOrders, name="TravelOrders"),
    path("Registration", Registration, name="Registration"),
    path("Login", Login, name="Login"),
    
]