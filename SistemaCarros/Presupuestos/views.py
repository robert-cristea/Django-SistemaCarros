from django.forms import formset_factory, modelform_factory
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView, UpdateView, CreateView, ListView, FormView, DetailView

from Clientes.forms import ClientesForm
from Clientes.models import Clientes
from Parte.forms import ParteForm
from carros.forms import CarroForm
from carros.models import Carro
from . import constants
from .forms import PresupuestosClientesForm, PresupuestosVehiculosForm, PresupuestosParteForm, PresupuestosManoObraForm, \
    PresupuestosPagosForm, PresupuestosFotosForm
#from .models import Presupuestos
 #Create your views here.
from .models import Presupuestos
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse_lazy





# class step1(CreateView):
#     model=Clientes
#     form_class = ClientesForm
#     template_name='Presupuestos/new-estimate-1-customer-details.html'
#     success_url=reverse_lazy('Presupuestos:step2')







def step1(request):
    extra_forms = 1
    presupuestosclientesform = PresupuestosClientesForm(request.POST or None)
    if request.method == 'POST':
        if presupuestosclientesform.is_valid():
            presupuestosclientesform.save()
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
    presupuestosparteform = PresupuestosParteForm(request.POST or None)
    if request.method == 'POST':
        print("======")
        print(request.POST)
        formset = ParteFormSet(request.POST, request.FILES)
        print("++++")
        print(formset)
        print("-------")
        print(presupuestosparteform)
        # formset = ParteFormSet(request.POST, request.FILES,prefix='__form')
        if formset.is_valid():
            presupuestosparteform.save()
            return redirect('Presupuestos:step4')
    else:
        formset = ParteFormSet()

    return render(request, 'Presupuestos/new-estimate-3-parts.html', {
        'presupuestosparteform': presupuestosparteform,
        'formset': formset,
    })

def step4(request):
    extra_forms = 1
    ManoObraFormSet = formset_factory(PresupuestosManoObraForm, extra=extra_forms, max_num=20)
    presupuestosmanoobraform = PresupuestosManoObraForm(request.POST or None)

    if request.method == 'POST':
        manoObra_formset = ManoObraFormSet(request.POST, request.FILES, prefix='manoobra')
        # formset = ParteFormSet(request.POST, request.FILES,prefix='__form')
        if manoObra_formset.is_valid():
            presupuestosmanoobraform.save()
            return redirect('Presupuestos:step5')
    else:
        manoObra_formset = ManoObraFormSet(prefix='manoobra')

    return render(request, 'Presupuestos/new-estimate-4-labor.html', {
        'presupuestosmanoobraform': presupuestosmanoobraform,
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
    presupuestospagosform=PresupuestosPagosForm(request.POST or None)
    PagosFormSet = formset_factory(PresupuestosPagosForm, extra=extra_forms, max_num=20)


    if request.method == 'POST':
        pagos_formset = PagosFormSet(request.POST, request.FILES, prefix='pagos')
        #formset = ParteFormSet(request.POST, request.FILES,prefix='__form')
        if pagos_formset.is_valid():
            presupuestospagosform.save()
            return redirect('Presupuestos:step7')
    else:
        pagos_formset = PagosFormSet(prefix='pagos')


    return render(request,'Presupuestos/new-estimate-6-payments.html',{
        'pagos_formset':pagos_formset
    })


#
# def step7(request):
#     presupuestosclientesform = get_object_or_404(Clientes, id=1)
#     presupuestosvehiculosform = get_object_or_404(Carro, id=1)
#
#     if request.method == 'POST':
#         presupuestosclientesform = PresupuestosClientesForm(request.POST, instance=presupuestosclientesform)
#         presupuestosvehiculosform = PresupuestosVehiculosForm(request.POST, instance=presupuestosvehiculosform)
#         if presupuestosclientesform.is_valid():
#             presupuestosclientesform.save()
#             return HttpResponseRedirect('/contacts/')
#
#     else:
#         presupuestosclientesform = PresupuestosClientesForm(instance=presupuestosclientesform)  # Here is the change
#         presupuestosvehiculosform = PresupuestosVehiculosForm(instance=presupuestosvehiculosform)  # Here is the change
#
#         return render(request, 'Presupuestos/new-estimate-7-preview.html', {'presupuestosclientesform':presupuestosclientesform,'presupuestosvehiculosform':presupuestosvehiculosform})
#




def step7(request, id):

    presupuestosclientes = Clientes.objects.get(id = id)
    presupuestoscarros = Carro.objects.get(id = id)
    context = {'presupuestosclientes': presupuestosclientes, 'presupuestoscarros': presupuestoscarros}
    return render(request, 'Presupuestos/new-estimate-7-preview.html', context)








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



class presupuestosIndex(ListView):
    model=Presupuestos
    template_name = 'Presupuestos/presupuestos.html'
    context_object_name='presupuestos'
    queryset=Presupuestos.objects.all()