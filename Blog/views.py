from django.http import HttpResponse
from django.template import loader

from django.shortcuts import render
from .models import Cities
from django.shortcuts import render, get_object_or_404


from django.contrib.auth import logout
from django.shortcuts import redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

def cities_list(request):
    cities = Cities.objects.all()  # Fetch all cities from the database
    return render(request, 'Cities.html', {'cities': cities})


def city_popular(request):
    city = Cities.objects.first() 
    return render(request, 'Home.html', {'city': city})

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


def Account(request):
    return render(request, 'account.html')

#def Main(request):
#  template = loader.get_template('Home.html')
#  return HttpResponse(template.render())




#def CityTemp(request):
#  template = loader.get_template('CityTemp.html')
#  return HttpResponse(template.render())

def Learn(request):
  template = loader.get_template('Learn.html')
  return HttpResponse(template.render())

def TravelOrders(request):
  template = loader.get_template('TravelOrders.html')
  return HttpResponse(template.render())



def Logout_View(request):
  logout(request)
  return redirect('Main')  # Redirect to home after logout

def Registration(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('Main')  # Redirect to home after successful registration
    else:
        form = UserCreationForm()
    return render(request, 'Registration.html', {'form': form})




#def Registration(request):
#  template = loader.get_template('Registration.html')
#  return HttpResponse(template.render())

#def Login(request):
#  template = loader.get_template('Login.html')
#  return HttpResponse(template.render())


def Login(request):
  if request.method == 'POST':
      form = AuthenticationForm(request, data=request.POST)
      if form.is_valid():
          user = form.get_user()
          login(request, user)
          return redirect('Account')  # Redirect to home after successful login
  else:
      form = AuthenticationForm()
  return render(request, 'Login.html', {'form': form})



