from .views import *
from django.urls import path
from . import views



urlpatterns = [
    path('', Main , name='Main'),
    path('Cities/<int:cities_id>/', views.CityTemp, name='CityTemp'),
   # path("Cities", CitiesPage, name="Cities"),
    path('cities/', views.cities_list, name='cities_list'),  # List of cities
    path('city/<int:id>/', views.city_detail, name='CityTemp'),  # City detail
    path("CityTemp", CityTemp, name="CityTemp"),
    path("Learn", Learn, name="Learn"),
    path("TravelOrders", TravelOrders, name="TravelOrders"),
    path("Registration", Registration, name="Registration"),
    path("Login", Login, name="Login"),
    
]