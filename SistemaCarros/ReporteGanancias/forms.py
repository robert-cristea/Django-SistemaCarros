from django import forms
from .models import ReporteGanancias


class ReporteGananciasForm(forms.ModelForm):
    class Meta:
        model=ReporteGanancias
        fields='__all__'