from .views import *
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views



urlpatterns = [
    path('', city_popular , name='Main'),
    path('Cities/<int:cities_id>/', views.CityTemp, name='CityTemp'),
   # path("Cities", CitiesPage, name="Cities"),
    path('cities/', views.cities_list, name='cities_list'),  # List of cities
    path('city/<int:id>/', views.city_detail, name='CityTemp'),  # City detail
    path("CityTemp", CityTemp, name="CityTemp"),
    path("Learn", Learn, name="Learn"),
    path("TravelOrders", TravelOrders, name="TravelOrders"),
    path("Registration", Registration, name="Registration"),
    path("Login", Login, name="Login"),
    path('Logout', Logout_View, name='Logout'),
    path('Account', Account, name='Account'),
    path('vocabulary-lists/', views.user_vocab_lists, name='user_vocab_lists'),
    path('vocabulary-list/<int:list_id>/', views.vocab_list_detail, name='vocab_list_detail'),
    path('create-vocabulary-list/', create_vocabulary_list, name='create_vocabulary_list'),
    path('add-words/<int:vocab_list_id>/', add_words, name='add_words'),
    path('preview-words/<int:vocab_list_id>/', preview_words, name='preview_words'),
    path('edit-vocabulary-list/<int:vocab_list_id>/', views.edit_vocabulary_list, name='edit_vocabulary_list'),
    path('delete-vocabulary-list/<int:vocab_list_id>/', views.delete_vocabulary_list, name='delete_vocabulary_list'),




]