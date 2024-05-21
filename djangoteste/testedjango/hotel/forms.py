from django import forms
from .models import TIPOS_QUARTOS


class CheckinForm(forms.Form):
    nome = forms.CharField(
        label="",
        max_length=20,
        widget=forms.TextInput(attrs={"class": "input", "placeholder": "Nome"}),
    )
    sobrenome = forms.CharField(
        label="",
        max_length=20,
        widget=forms.TextInput(attrs={"class": "input", "placeholder": "Sobrenome"}),
    )
    email = forms.EmailField(
        label="",
        max_length=50,
        widget=forms.EmailInput(attrs={"class": "input", "placeholder": "Email"}),
    )
    tipo_quarto = forms.ChoiceField(
        label="",
        choices=TIPOS_QUARTOS,
        widget=forms.Select(attrs={"class": "input", "placeholder": "Tipo de quarto"}),
    )
    data_reserva = forms.DateField(
        label="",
        widget=forms.SelectDateWidget(
            attrs={"class": "input", "placeholder": "Data de reserva"}
        ),
    )


class CadastroForm(forms.Form):
    username = forms.CharField(
        label="",
        max_length=20,
        widget=forms.TextInput(attrs={"class": "input", "placeholder": "Username"}),
    )

    nome = forms.CharField(
        label="",
        max_length=20,
        widget=forms.TextInput(attrs={"class": "input", "placeholder": "Nome"}),
    )
    sobrenome = forms.CharField(
        label="",
        max_length=20,
        widget=forms.TextInput(attrs={"class": "input", "placeholder": "Sobrenome"}),
    )
    email = forms.EmailField(
        label="",
        max_length=50,
        widget=forms.EmailInput(attrs={"class": "input", "placeholder": "Email"}),
    )
    senha = forms.CharField(
        label="",
        max_length=20,
        widget=forms.PasswordInput(attrs={"class": "input", "placeholder": "Senha"}),
    )


class LoginForm(forms.Form):
    username = forms.CharField(
        label="",
        max_length=20,
        widget=forms.TextInput(attrs={"class": "input", "placeholder": "User"}),
    )
    senha = forms.CharField(
        label="",
        max_length=20,
        widget=forms.PasswordInput(attrs={"class": "input", "placeholder": "Senha"}),
    )