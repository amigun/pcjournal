from django.contrib.auth.forms import AuthenticationForm
from django import forms

class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Юзернейм', widget=forms.TextInput(attrs={'class': 'p-3 rounded-md bg-blue-100 shadow-xl shadow-blue-100 text-blue-500 w-full mb-5 transition focus:shadow-blue-100/50 focus:outline-none'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'p-3 rounded-md bg-blue-100 shadow-xl shadow-blue-100 text-blue-500 w-full mb-5 transition focus:shadow-blue-100/50 focus:outline-none'}))