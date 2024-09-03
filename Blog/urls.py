from .views import *
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

from django.conf.urls import handler404
from .views import custom_page_not_found,update_profile


handler404 = custom_page_not_found

urlpatterns = [
    path('', city_popular , name='Main'),
    path('Cities/<int:cities_id>/', views.CityTemp, name='CityTemp'),
    path('cities/', views.cities_list, name='cities_list'),  # List of cities
    path('city/<int:id>/', city_detail, name='CityTemp'),  # City detail
    path("CityTemp", CityTemp, name="CityTemp"),
    path("Learn", Learn, name="Learn"),
    path("Registration", Registration, name="Registration"),
    path("Login", Login, name="Login"),
    path('Logout', Logout_View, name='Logout'),
    path('Account', Account, name='Account'),
    path('update-profile/', update_profile, name='update_profile'),


]