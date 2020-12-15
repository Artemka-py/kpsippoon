from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=60, help_text='Введите e-mail')

    class Meta:
        model = User
        fields = ('email', 'username', 'password1', 'password2')