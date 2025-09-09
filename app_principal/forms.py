from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class FormularioCriacaoUsuario(UserCreationForm):
    email = forms.EmailField(required=True)
    is_staff = forms.BooleanField(required=False, label="Administrador?")
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'is_staff']
