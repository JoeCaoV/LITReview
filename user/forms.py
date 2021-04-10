from django.forms import ModelForm, TextInput, PasswordInput
from .models import User


class UserLogin(ModelForm):
    class Meta:
        model = User
        fields = ["email", "password"]
        widget = {
            'email': TextInput(attrs={'class': 'form-control'}),
            'password': PasswordInput(attrs={'placeholder': 'Password', 'class': 'form-control'}),
        }


class UserRegistration(ModelForm):
    class Meta:
        model = User
        fields = ["email", "password"]
        widget = {
            'email': TextInput(attrs={'class': 'form-control'}),
            'password': PasswordInput(attrs={'placeholder': 'Password', 'class': 'form-control', 'type': 'password'}),

        }
