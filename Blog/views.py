from django.http import HttpResponse
from django.template import loader

from .models import Cities,Comment
from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.decorators import login_required


from django.contrib.auth import logout
from django.shortcuts import redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .forms import CustomUserCreationForm,ProfileUpdateForm,CommentForm


from django.contrib.auth.decorators import login_required

from django.http import JsonResponse






def cities_list(request):
    cities = Cities.objects.all()  # Fetch all cities from the database
    return render(request, 'Cities.html', {'cities': cities})


def city_popular(request):
    city = Cities.objects.first() 
    return render(request, 'Home.html', {'city': city})

#def city_detail(request, id):
#    city = get_object_or_404(Cities, id=id)
#    return render(request, 'CityTemp.html', {'city': city})



@login_required
def city_detail(request, id):
    city = get_object_or_404(Cities, id=id)
    comments = city.comments.all()
    
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.city = city
            comment.author = request.user  # Set the current logged-in user as the comment author
            comment.save()
            return redirect('CityTemp', id=city.id)  # Redirect to avoid resubmission on refresh
    else:
        form = CommentForm()
    
    return render(request, 'CityTemp.html', {
        'city': city,
        'comments': comments,
        'form': form
    })

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
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('Main')  # Redirect to home after successful registration
    else:
        form = CustomUserCreationForm()
    return render(request, 'Registration.html', {'form': form})



@login_required
def profile_update(request):
    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, request.FILES)
        if form.is_valid():
            profile, created = Profile.objects.get_or_create(user=request.user)
            profile.bio = form.cleaned_data['bio']
            profile.location = form.cleaned_data['location']
            if 'avatar' in request.FILES:
                profile.avatar = request.FILES['avatar']
            profile.save()
            
            # Return JSON response for AJAX request
            if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                return JsonResponse({'success': True})
            
            return redirect('profile')  # Redirect if not an AJAX request
        
        # Return JSON response for AJAX request with form errors
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            return JsonResponse({'success': False, 'errors': form.errors})

    # Render the form for non-AJAX requests
    return render(request, 'profile_update.html', {'form': ProfileUpdateForm()})



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



