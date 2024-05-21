from django import forms


class CheckinForm(forms.Form):
    nome = forms.CharField(label="Nome", max_length=20)
    email = forms.EmailField(label="Email", max_length=50)