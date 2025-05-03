from django import forms
from django.contrib.auth.forms import PasswordResetForm, UserCreationForm
from .models import *



class SignUpForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ['username', 'email']

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class CustomPasswordResetForm(PasswordResetForm):
    email = forms.EmailField()