from django.http import HttpResponse
from django.template import loader

from .models import Cities
from django.shortcuts import render,redirect, get_object_or_404


from django.contrib.auth import logout
from django.shortcuts import redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

from django.contrib.auth.decorators import login_required
from .models import VocabularyList, VocabularyWord
from .forms import VocabularyListForm, VocabularyWordForm

@login_required
def create_vocabulary_list(request):
    if request.method == 'POST':
        form = VocabularyListForm(request.POST)
        if form.is_valid():
            vocab_list = form.save(commit=False)
            vocab_list.user = request.user
            vocab_list.save()
            return redirect('add_words', vocab_list_id=vocab_list.id)
    else:
        form = VocabularyListForm()
    return render(request, 'create_vocabulary_list.html', {'form': form})

@login_required
def add_words(request, vocab_list_id):
    vocab_list = get_object_or_404(VocabularyList, id=vocab_list_id)
    if request.method == 'POST':
        form = VocabularyWordForm(request.POST)
        if form.is_valid():
            word = form.save(commit=False)
            word.vocab_list = vocab_list
            word.save()
            if vocab_list.words.count() >= 50:
                return redirect('preview_words', vocab_list_id=vocab_list.id)
    else:
        form = VocabularyWordForm()
    return render(request, 'add_words.html', {'form': form, 'vocab_list': vocab_list})

def preview_words(request, vocab_list_id):
    vocab_list = get_object_or_404(VocabularyList, id=vocab_list_id)
    words = vocab_list.words.all()[:50]
    return render(request, 'preview_words.html', {'vocab_list': vocab_list, 'words': words})

@login_required
def edit_vocabulary_list(request, vocab_list_id):
    vocab_list = get_object_or_404(VocabularyList, id=vocab_list_id)
    if request.method == 'POST':
        form = VocabularyListForm(request.POST, instance=vocab_list)
        if form.is_valid():
            form.save()
            return redirect('preview_words', vocab_list_id=vocab_list.id)
    else:
        form = VocabularyListForm(instance=vocab_list)
    return render(request, 'edit_vocabulary_list.html', {'form': form, 'vocab_list': vocab_list})

@login_required
def delete_vocabulary_list(request, vocab_list_id):
    vocab_list = get_object_or_404(VocabularyList, id=vocab_list_id)
    if request.method == 'POST':
        vocab_list.delete()
        return redirect('home')
    return render(request, 'delete_vocabulary_list.html', {'vocab_list': vocab_list})


# View for the user's vocabulary lists
def user_vocab_lists(request):
    vocab_lists = VocabularyList.objects.filter(user=request.user)  # Filter lists by the logged-in user
    return render(request, 'user_vocab_lists.html', {'vocab_lists': vocab_lists})

# View for details of a specific vocabulary list
def vocab_list_detail(request, list_id):
    vocab_list = get_object_or_404(VocabularyList, id=list_id, user=request.user)
    return render(request, 'vocab_list_detail.html', {'vocab_list': vocab_list})





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



