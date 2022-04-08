import datetime

from django.forms import formset_factory, modelform_factory
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView, UpdateView, CreateView, ListView, FormView, DetailView

from Clientes.forms import ClientesForm
from Clientes.models import Clientes
from ManoObra.models import ManoObra
from Parte.forms import ParteForm
from Parte.models import Parte
from carros.forms import CarroForm
from carros.models import Carro
from Pagos.models import Pagos
from tecnicos.models import Tecnicos
from . import constants
from .forms import PresupuestosClientesForm, PresupuestosVehiculosForm, PresupuestosParteForm, PresupuestosManoObraForm, \
    PresupuestosPagosForm, PresupuestosForm
#from .models import Presupuestos
 #Create your views here.
from .models import Presupuestos
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse_lazy










def step1(request):
    presupuestosclientesform = PresupuestosClientesForm(request.POST or None)
    if request.method == 'POST':
        print(request.POST.get('titulo'))
        if presupuestosclientesform.is_valid():
            presupuestosclientesform.save()
            current_customer=Clientes.objects.all().last()
            request.session['client_id']=current_customer.id
            return redirect('Presupuestos:step2')
    else:
        presupuestosclientesform = PresupuestosClientesForm(request.POST or None)

    return render(request,'Presupuestos/new-estimate-1-customer-details.html',{
        'presupuestosclientesform':presupuestosclientesform,

    })




def step2(request):
    presupuestosvehiculosform=PresupuestosVehiculosForm(request.POST or None)
    if request.method == 'POST':
        if presupuestosvehiculosform.is_valid():
            presupuestosvehiculosform.save()
            request.session['car_id']=Carro.objects.all().last().id
            return redirect('Presupuestos:step3')
    else:
        presupuestosvehiculosform=PresupuestosVehiculosForm(request.POST or None)

    return render(request,'Presupuestos/new-estimate-2-vehicle.html',{
        'presupuestosvehiculosform':presupuestosvehiculosform,

    })



# class step2(CreateView):
#     model=Carro
#     form_class=CarroForm
#     template_name='Presupuestos/new-estimate-2-vehicle.html'
#     success_url=reverse_lazy('Presupuestos:step3')


def step3(request):

    extra_forms = 1
    ParteFormSet = formset_factory(PresupuestosParteForm, extra=extra_forms, max_num=20)
    presupuestosform = PresupuestosForm(request.POST or None)
    if request.method == 'POST':
        request.session['resumen'] = request.POST['resumen']
        request.session['descuento_parte'] = request.POST['descuento_parte']
        request.session['descuentoTotal_parte'] = request.POST['descuentoTotal_parte']
        request.session['total_parte'] = request.POST['total_parte']
        formset = ParteFormSet(request.POST, request.FILES, prefix='form')
        request.session['number_parte'] = request.POST['form-TOTAL_FORMS']
        if formset.is_valid():

            for form in formset:
                form.save()
            return redirect('Presupuestos:step4')
    else:
        formset = ParteFormSet()

    return render(request, 'Presupuestos/new-estimate-3-parts.html', {
        'presupuestosform':presupuestosform,
        'formset': formset,
    })

def step4(request):
    extra_forms = 1
    ManoObraFormSet = formset_factory(PresupuestosManoObraForm, extra=extra_forms, max_num=20)
    presupuestosform = PresupuestosForm(request.POST or None)

    if request.method == 'POST':
        request.session['descuento_manaobra'] = request.POST['descuento_manaobra']
        request.session['descuentoTotal_manaobra'] = request.POST['descuentoTotal_manaobra']
        request.session['total_monaobra'] = request.POST['total_manaobra']
        manoObra_formset = ManoObraFormSet(request.POST, request.FILES, prefix='manoobra')
        request.session['number_labor'] = request.POST['manoobra-TOTAL_FORMS']
        print(manoObra_formset.errors)
        if manoObra_formset.is_valid():
            for form in manoObra_formset:
                form.save()
            return redirect('Presupuestos:step5')
    else:
        manoObra_formset = ManoObraFormSet(prefix='manoobra')

    return render(request, 'Presupuestos/new-estimate-4-labor.html', {
        'presupuestosform': presupuestosform,
        'manoObra_formset': manoObra_formset,

    })

def step5(request):
    Vehicle=Carro.objects.all().last()
    if request.method == 'POST':
            Vehicle.fotosCarro=request.POST['fotoscarro']
            Vehicle.save()
            return redirect('Presupuestos:step6')
    return render(request, 'Presupuestos/new-estimate-5-pictures.html')

def step6(request):
    extra_forms = 1
    PagosFormSet = formset_factory(PresupuestosPagosForm, extra=extra_forms, max_num=20)
    if request.method == 'POST':
        pagos_formset = PagosFormSet(request.POST, request.FILES, prefix='pagos')
        if pagos_formset.is_valid():
            request.session['number_pago']=request.POST['pagos-TOTAL_FORMS']
            for form in pagos_formset:
                form.save()
            return redirect('Presupuestos:step7')
    else:
        pagos_formset = PagosFormSet(prefix='pagos')


    return render(request,'Presupuestos/new-estimate-6-payments.html',{
        'pagos_formset':pagos_formset
    })


#
def step7(request):
    technicans = Tecnicos.objects.all()
    step_client = Clientes.objects.get(pk=request.session['client_id'])
    step_vehicle = Carro.objects.get(pk=request.session['car_id'])
    step_parte = reversed(Parte.objects.all().order_by('-id')[:int(request.session['number_parte'])])
    step_manoobra = reversed(ManoObra.objects.all().order_by('-id')[:int(request.session['number_labor'])])
    step_pago = Pagos.objects.all().order_by('-id')[:int(request.session['number_pago'])]
    payment = 0
    for step in step_pago:
        payment += step.cantidad_pagada
    total = int(request.session['total_parte']) + int(request.session['total_manaobra'])
    balance = total - payment
    time=datetime.datetime.now()
    if request.method=='POST':
        presupuestos=Presupuestos()
        presupuestos.resumen=request.session['resumen']
        presupuestos.total_parte=int(request.session['total_parte'])
        presupuestos.total_manaobra=int(request.session['total_manaobra'])
        presupuestos.descuento_parte=request.session['descuento_parte']
        presupuestos.descuentoTotal_parte=int(request.session['descuentoTotal_parte'])
        presupuestos.descuentoTotal_manaobra=int(request.session['descuentoTotal_manaobra'])
        presupuestos.descuento_manaobra=request.session['descuento_manaobra']
        presupuestos.register_time=time
        presupuestos.cliente_id=request.session['client_id']
        presupuestos.carro_id=request.session['car_id']
        print(request.POST['technican_select'])
        presupuestos.tecnicos_id=request.POST['technican_select']
        presupuestos.save()
        return redirect('Presupuestos:step8')
    else:
        return render(request, 'Presupuestos/new-estimate-7-preview.html',
                  {'technicans': technicans, 'step_client': step_client, 'step_vehicle': step_vehicle,
                   'step_parte': step_parte, 'step_manoobra': step_manoobra, 'balance': balance, 'total': total,'time':time})


class step8(TemplateView):
    template_name='Presupuestos/new-estimate-8-confirm.html'



class addPay(CreateView):
    model=Presupuestos
    form_class=PresupuestosPagosForm
    template_name='Presupuestos/presupuestos-add-payment.html'
    success_url=reverse_lazy('InformacionTiendas:list_tiendas')


class addPart(CreateView):
    model=Presupuestos
    form_class=PresupuestosParteForm
    template_name='Presupuestos/presupuestos-add-parts.html'
    success_url=reverse_lazy('InformacionTiendas:list_tiendas')


class addLabor(CreateView):
    model=Presupuestos
    form_class=PresupuestosManoObraForm
    template_name='Presupuestos/presupuestos-add-labor.html'
    success_url=reverse_lazy('InformacionTiendas:list_tiendas')



def presupuestosIndex(request):
    presupuestos_all=Presupuestos.objects.all()
    temp=Presupuestos.objects.all().last()
    return render(request, 'Presupuestos/presupuestos.html',{'prespuestos':presupuestos_all})