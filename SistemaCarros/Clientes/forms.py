from django import forms
from Clientes.models import Clientes


PAIS = (
    ('United States', 'United States'),
    ('Canada', 'Canada'),
    ('Other', 'Other'),
)

TIPO = (
    ('Corporativo', 'Corporativo'),
    ('Persona', 'Persona'),
)





class ClientesForm(forms.ModelForm):

    tipo = forms.ChoiceField(
        choices=TIPO,
        widget=forms.RadioSelect(attrs={'class':'custom-radio-list'}),

    )

    pais = forms.ChoiceField(
        choices=PAIS,
        widget=forms.RadioSelect(attrs={'class':'custom-radio-list'}),

    )


    class Meta:
        model = Clientes
        fields = ['titulo','tipo','nombre', 'apellido', 'telefono', 'tel', 'fax', 'correo', 'direccion','pais',
                  'ciudad','estado','zip','corporacion', 'website','social_media','social_media2','social_media3',
                   'contacto_alternativo','contacto_alternativo2','contacto_alternativo3',]
        exclude = ['fecha_registro']
        widgets = {

            'titulo': forms.Select(
                attrs={
                    'class': 'form-select'
                }
            ),
            'corporacion': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'nombre': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'apellido': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'telefono': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'tel': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'fax': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'correo': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),

            'website': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'social_media': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'social_media2': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'social_media3': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'contacto_alternativo': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'contacto_alternativo2': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'contacto_alternativo3': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),

            'direccion': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'ciudad': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'estado': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'zip': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'fecha_registro': forms.DateInput(
                attrs={
                    'class': 'form-control',
                }
            ),

        }

class DateRangeForm(forms.Form):
    start_date = forms.DateField()
    end_date = forms.DateField()