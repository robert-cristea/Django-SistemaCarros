from django import forms
from django.forms import formset_factory

from Clientes import models
from Foto.models import Foto
from Parte.forms import ParteForm
from Presupuestos.models import Presupuestos
from carros.models import Carro
from  Clientes.models import Clientes
from  Parte.models import Parte
from  ManoObra.models import ManoObra
from  Pagos.models import Pagos
from tecnicos.models import Tecnicos

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
        }


class PresupuestosVehiculosForm(forms.ModelForm):


    class Meta:
        model = Carro
        fields = ['placas','año','modelo','marca','tipo','motor','vin','color','fotosCarro']
        exclude = ['agente_seguros', 'compañia_seguros','no_politica','garantia',
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
            'fotosCarro':forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'id': 'car-input'
                }
            ),


        }




class PresupuestosParteForm(forms.ModelForm):
    class Meta:
        model = Parte
        fields = ['codigo','quantity','unit_price','total_price','tax_free','comprado_cliente','descripcion','descuento_parte']
        exclude = ['estimate_id']
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
            'descuento_parte': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'id': 'id__form-0-descuento_parte',
                    'onchange': 'descuentoParte(multiplicar())',
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
        fields = ['codigo','tecnico','tarifa','tarifa_total','horas','minutos','libre_impuestos','descripcion']
        exclude = ['estimate_ids']
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
            'descripcion': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),

        }
    def __init__(self, *args, **kwargs):
        super(PresupuestosManoObraForm, self).__init__(*args, **kwargs)
        technicans = Tecnicos.objects.all()
        technico = [(i.nombreTecnico,i.apellidoTecnico) for i in technicans]
        self.fields['tecnico'] = forms.ChoiceField(choices=technico)



class PresupuestosPagosForm(forms.ModelForm):
    class Meta:
        model = Pagos
        fields = ['tipo_pago','cantidad_pagada','numero_transaccion']
        exclude = ['estimate']
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

class PresupuestosForm(forms.ModelForm):
    class Meta:
        model = Presupuestos
        fields = ['descuento_parte','descuentoTotal_parte','total_parte','resumen','descuento_manaobra','descuentoTotal_manaobra','total_manaobra']
        widgets = {
             'descuento_parte': forms.RadioSelect(choices=DISCOUNT,
                 attrs={
                    'class': "custom-radio-list"
                 }
            ),
            'descuentoTotal_parte': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'onchange': 'descuentoTotalFuncion()',
                    'placeholder': 'put the number',

                }
            ),
            'total_parte': forms.NumberInput(
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
            'descuento_manaobra': forms.RadioSelect(choices=DISCOUNT,
                attrs={
                    'class': "custom-radio-list"
                }
            ),
            'descuentoTotal_manaobra': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'onchange': 'descuentoTotalFuncion()',
                    'placeholder': 'put the number',

                }
            ),
            'total_manaobra': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': '$0.00',
                }
            ),

        }