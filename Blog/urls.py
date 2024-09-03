from .views import *
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views



urlpatterns = [
    path('', city_popular , name='Main'),
    path('Cities/<int:cities_id>/', views.CityTemp, name='CityTemp'),
    path('cities/', views.cities_list, name='cities_list'),  # List of cities
    path('city/<int:id>/', city_detail, name='CityTemp'),  # City detail
    path("CityTemp", CityTemp, name="CityTemp"),
    path("Learn", Learn, name="Learn"),
    path("TravelOrders", TravelOrders, name="TravelOrders"),
    path("Registration", Registration, name="Registration"),
    path("Login", Login, name="Login"),
    path('Logout', Logout_View, name='Logout'),
    path('Account', Account, name='Account'),
    path('Account', profile_update, name='update_profile'),


]