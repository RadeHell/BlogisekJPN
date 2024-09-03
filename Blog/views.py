from django.http import HttpResponse
from django.template import loader

from .models import Cities,Comment
from django.shortcuts import render,redirect, get_object_or_404,redirect
from django.contrib.auth.decorators import login_required


from django.contrib.auth import logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from .forms import CustomUserCreationForm,CommentForm


from django.contrib.auth.decorators import login_required

from django.http import JsonResponse, HttpResponseNotFound
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from .forms import UserProfileForm


def custom_page_not_found(request, exception=None):
    template = loader.get_template('404.html')
    return HttpResponseNotFound(template.render({}, request))


def cities_list(request):
    cities = Cities.objects.all()  # Fetch all cities from the database
    return render(request, 'Cities.html', {'cities': cities})


def city_popular(request):
    city = Cities.objects.first() 
    return render(request, 'Home.html', {'city': city})



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



def CityTemp(request):
    cities = Cities.objects.first()
    return render(request, 'CityTemp.html', {'cities': cities})



def Account(request):
    return render(request, 'account.html')



def Learn(request):
  template = loader.get_template('Learn.html')
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
@require_POST
def update_profile(request):
    try:
        profile = request.user.profile
        
        # Get fields from the request
        avatar_url = request.POST.get('avatar')
        bio = request.POST.get('bio')
        location = request.POST.get('location')

        # Update profile fields only if they are provided
        if avatar_url:
            profile.avatar = avatar_url
        if bio:
            profile.bio = bio
        if location:
            profile.location = location
        
        profile.save()

        return JsonResponse({'success': True})
    except Exception as e:
        return JsonResponse({'success': False, 'errors': str(e)}, status=400)



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



