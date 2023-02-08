from django import forms
from .models import Registrado

class RegModelForm(forms.ModelForm):
    class meta:
        Model = Registrado
        fields = ["nombre", "email"]


class RegistradoForm(forms.Form):
    nombre = forms.CharField(max_length=120)
    email = forms.EmailField()