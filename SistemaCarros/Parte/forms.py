from django import forms
from django.forms import formset_factory

from .models import Parte


class ParteForm(forms.ModelForm):
    class Meta:
        model=Parte
        fields=['codigo','descripcion','quantity','unit_price','total_price','tax_free','comprado_cliente']


