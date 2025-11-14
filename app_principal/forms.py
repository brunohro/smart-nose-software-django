from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import TipoSensor
from django.contrib.auth.hashers import make_password
class FormularioCriacaoUsuario(forms.ModelForm):
    confirm_password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ["first_name", "username", "email", "password", "is_staff"]
        widgets = {
            "password": forms.PasswordInput(),
        }
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise forms.ValidationError("As senhas não coincidem.")

        cleaned_data["password"] = make_password(password)
        return cleaned_data
    
class FormularioCriacaoSensor(forms.ModelForm):
    SIM_NAO = [
        (True, 'Sim'),
        (False, 'Não')
    ]

    nome = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Ex: MQ2, Sensor de Gás, Temperatura Interna...'
        }),
        label='Nome do Sensor'
    )

    exibir = forms.ChoiceField(
        choices=SIM_NAO,
        widget=forms.Select(attrs={'class': 'form-control'}),
        label='Exibir sensor'
    )

    class Meta:
        model = TipoSensor
        fields = ['nome', 'funcao', 'exibir']
        widgets = {
            'funcao': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Descreva a função do sensor'
            }),
        }

    def clean_exibir(self):
        valor = self.cleaned_data['exibir']
        return True if valor in ['True', True, 'Sim'] else False