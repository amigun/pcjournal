from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import render

# Create your views here.
from .forms import *


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'login/login.html'