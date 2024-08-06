from django.urls import path
from .views import *


urlpatterns = [
    path('', Main , name='Main'),
    path("Map", Map, name="Map"),
    path("TravelOrders", TravelOrders, name="TravelOrders"),
    path("Registration", Registration, name="Registration"),
    path("Login", Login, name="Login"),
]