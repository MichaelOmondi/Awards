from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from pyuploadcare.dj.forms import ImageField

from .models import Profile, Project, Rate

class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "password1", "password2"]

class UpdateUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email')

