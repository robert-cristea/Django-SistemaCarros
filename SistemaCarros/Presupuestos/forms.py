from django import forms
from django.forms import formset_factory

from Clientes import models
from Foto.models import Foto
from Parte.forms import ParteForm
from carros.models import Carro
from  Clientes.models import Clientes
from  Parte.models import Parte
from  ManoObra.models import ManoObra
from  Pagos.models import Pagos


DESCUENTO = (
    ('Quantity', 'Quantity'),
    ('Percentage', 'Percentage'),
)

DISCOUNT= (
    ('Quantity', 'Quantity'),
    ('Percentage', 'Percentage'),
)





class PresupuestosClientesForm(forms.ModelForm):

    class Meta:
        model = Clientes
        fields = ['titulo', 'nombre','apellido','correo','telefono','tel']
        exclude = ['corporacion', 'fax','website','social_media','social_media2',
                   'social_media3','contacto_alternativo','contacto_alternativo2','contacto_alternativo3',
                   'pais','direccion','ciudad','estado','zip']
        widgets = {
            'titulo': forms.Select(
                attrs={
                    'class': 'form-select'
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
            'correo': forms.EmailInput(
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
            'notas': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
        }


class PresupuestosVehiculosForm(forms.ModelForm):


    class Meta:
        model = Carro
        fields = ['placas','año','modelo','marca','tipo','motor','vin','color']
        exclude = ['agente_seguros', 'compañia_seguros','no_politica','fotosCarro','garantia',
                   'cliente','fecha_registros']
        widgets = {
            'placas': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'año': forms.NumberInput(
                attrs={
                    'class': 'form-control'
                }
            ),

            'modelo':forms.TextInput(
                attrs={
                    'class':'form-control'
                }
            ),
            'marca': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'tipo': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'motor': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'vin': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'color': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),

        }




class PresupuestosParteForm(forms.ModelForm):
    class Meta:
        model = Parte
        fields = '__all__'

        widgets = {
            'codigo': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'id': 'id__form-0-codigo',
                }
            ),
            'quantity': forms.NumberInput(
                attrs={
                    'class': 'form-control-quantity',
                    'id':'id__form-0-quantity',
                }
            ),
            'unit_price': forms.NumberInput(
                attrs={
                    'class': 'form-control-unit-price',
                    'id': 'id__form-0-unit_price',
                    'onchange': 'multiplicar()',
                }
            ),
            'total_price': forms.NumberInput(
                attrs={
                    'class': 'form-control-total-price',
                    'id': 'id__form-0-total_price',

                }
            ),
            'tax_free': forms.CheckboxInput(
                attrs={
                    'class': 'form-check-input',
                    'onclick': 'taxes_free(multiplicar())',
                    'id': 'id__form-0-tax_free',
                }
            ),
            'comprado_cliente': forms.CheckboxInput(
                attrs={
                    'class': 'form-check-input',
                    'onclick': 'taxes_free(descuentoParte())',
                    'id': 'id__form-0-comprado_cliente',
                }
            ),
            'descripcion': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'id': 'id__form-0-descripcion',
                }
            ),
            'descuento': forms.RadioSelect(choices=DISCOUNT,
                 attrs={
                    'class': "custom-radio-list"
                 }
            ),
            'descuentoTotal': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'onchange': 'descuentoTotalFuncion()',
                    'placeholder': 'put the number',

                }
            ),

            'descuento_parte': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'id': 'id__form-0-descuento_parte',
                    'onchange': 'descuentoParte(multiplicar())',
                }
            ),
            'total': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': '$0.00',
                }
            ),

            'resumen': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'rows': 2, 'cols': 5,
                }
            ),

        }
    # def __init__(self):
    #     helper = FormHelper()
    #     helper.form_show_labels = False

#ParteFormset = formset_factory(ParteForm, extra=1)

class PresupuestosManoObraForm(forms.ModelForm):
    class Meta:
        model = ManoObra
        fields = '__all__'
        widgets = {
            'codigo': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'id': 'id__manoobra-0-codigo',
                }
            ),
            'tecnico': forms.Select(
                attrs={
                    'class': 'form-select',
                    'id': 'id__manoobra-0-tecnico',
                }
            ),
            'tarifa_hora': forms.NumberInput(
                attrs={
                    'class': 'form-control'

                }
            ),
            'horas': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'id': 'id__manoobra-0-horas',
                }
            ),
            'minutos': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'onchange': 'convMinHr()',
                    'id': 'id__manoobra-0-minutos',
                }
            ),
            'tarifa': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'onchange': 'convTarifa(convMinHr())',
                    'id': 'id__manoobra-0-tarifa',
                }
            ),
            'tarifa_total': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'id': 'id__manoobra-0-tarifa_total',
                }
            ),
            'libre_impuestos': forms.CheckboxInput(
                attrs={
                    'class': 'form-check-input',
                    'id': 'id__manoobra-0-libre_impuestos',
                    'onchange': 'taxes_freez(addFormz())',

                }
            ),

            'descuento': forms.RadioSelect(choices=DESCUENTO,
                 attrs={
                    'class': "custom-radio-list"
                 }
            ),
            'numeroDescuento': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'put the number',
                    'onchange': 'Discountz(taxes_freez())',

                }
            ),
            'total': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder':'$0.00',
                    'id':'totals',
                }
            ),
            'partsDiscount': forms.NumberInput(
                attrs={
                    'class': 'form-control',

                }
            ),
            'descripcion': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),

        }



class PresupuestosPagosForm(forms.ModelForm):
    class Meta:
        model = Pagos
        fields = '__all__'
        widgets = {
            'tipo_pago': forms.Select(
                attrs={
                    'class': 'form-select'
                }
            ),
            'cantidad_pagada': forms.NumberInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'numero_transaccion': forms.NumberInput(
                attrs={
                    'class': 'form-control'
                }
            ),

        }

class PresupuestosFotosForm(forms.ModelForm):
    class Meta:
        model = Foto
        fields = '__all__'
        widgets = {
            'imagenes': forms.FileInput(
                attrs={
                    'class': 'form-control',
                    'multiple': True
                }
            ),
        }