from django.http import HttpResponse
from django.template import loader

from django.shortcuts import render
from .models import Cities
from django.shortcuts import render, get_object_or_404

def cities_list(request):
    cities = Cities.objects.all()  # Fetch all cities from the database
    return render(request, 'Cities.html', {'cities': cities})

def city_detail(request, id):
    city = get_object_or_404(Cities, id=id)
    return render(request, 'CityTemp.html', {'city': city})


#def CitiesPage(request):
#    cities = Cities.objects.filter(id=1)  # Fetch all cities from the database
#    return render(request, 'Cities.html', {'cities': cities})

def CityTemp(request):
    cities = Cities.objects.first()
    return render(request, 'CityTemp.html', {'cities': cities})



#def CitiesPage(request):
#  cities = Cities.objects.first()
#  return render(request, 'Cities.html', {'cities': cities})




def Main(request):
  template = loader.get_template('Home.html')
  return HttpResponse(template.render())




#def CityTemp(request):
#  template = loader.get_template('CityTemp.html')
#  return HttpResponse(template.render())

def Learn(request):
  template = loader.get_template('Learn.html')
  return HttpResponse(template.render())

def TravelOrders(request):
  template = loader.get_template('TravelOrders.html')
  return HttpResponse(template.render())

def Registration(request):
  template = loader.get_template('Registration.html')
  return HttpResponse(template.render())

def Login(request):
  template = loader.get_template('Login.html')
  return HttpResponse(template.render())