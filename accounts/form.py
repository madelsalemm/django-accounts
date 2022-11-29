from dataclasses import fields
import imp
from importlib.metadata import files
from django import forms
from .models import Profile
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class SignupForm (UserCreationForm):
    class Meta:
        model = User
        fields = ['username' , 'email' , 'password1' , 'password2']
        
        
class UserForm (forms.ModelForm):
    class Meta:
        model = User
        fields = ['username' , 'first_name' , 'last_name' , 'email']
    

class ProfileForm (forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['phonenumber' , 'address']
        



