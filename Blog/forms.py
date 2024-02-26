from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    class meta:
        model =User
        fields =['username','password1','password2']

class LoginForm(AuthenticationForm):
    class meta:
        model =User
        fields = ['username','password1']