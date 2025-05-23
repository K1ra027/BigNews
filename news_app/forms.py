from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from django import forms



class RegistrationForm(UserCreationForm):
    class Meta:
        model =User
        fields =['first_name','last_name','username','password1','password2']




class LoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username','password']