from django import forms
from  ManoObra.models import ManoObra


class ManoObraForm(forms.ModelForm):
    class Meta:
        model=ManoObra
        fields=['codigo','tecnico','tarifa_hora','horas','minutos','tarifa','tarifa_hora',
                'libre_impuestos','descuento','total','descripcion']