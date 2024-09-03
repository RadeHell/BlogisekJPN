from django import forms
from .models import Comment,Profile



from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=False, help_text='Optional.')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')



class UserProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['avatar', 'bio', 'location']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
