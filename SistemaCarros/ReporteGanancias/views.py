from django.core.mail import send_mail
from django.forms import formset_factory
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.template import loader
from django.views.generic import TemplateView, ListView
import json
# from inventory.models import Inventory
from ManoObra.models import ManoObra
from Presupuestos.forms import PresupuestosPagosForm, PresupuestosParteForm, PresupuestosForm, PresupuestosManoObraForm
from Presupuestos.models import Presupuestos
from carros.models import Carro
from invoices.models import Invoices
from .forms import ReporteGananciasForm
from django.db.models import Count

# Create your views here.
from .models import ReporteGanancias
from .models import Parte


class IndexReporteGanancias(TemplateView):
    template_name='ReporteGanancias/list.html'



def reportsDebtors(request):
    if request.method =='POST':
        fromdate=request.POST['fromdate']
        todate=request.POST['todate']
        presupuestos_all=Presupuestos.objects.filter(register_time__range=(fromdate,todate))
    else:
        presupuestos_all = Presupuestos.objects.all()
    send_data = {'presupuestos': presupuestos_all}

    if request.session.get("messages"):
        send_data = {
            'presupuestos': presupuestos_all,
            'messages': request.session.get("messages")
        }
        request.session.pop("messages")

    return render(request, "ReporteGanancias/reports-debtors.html",
                  send_data)

def send_email(request,pk):
    presupuesto = Presupuestos.objects.get(pk=pk)
    html_message = loader.render_to_string(
        'Presupuestos/estimate-pdf.html',
        {'presupuesto': presupuesto}
    )
    email_subject = 'Your Estimate!'
    to_list = 'customer@dinh.mail.com'
    send_mail(email_subject, 'message', None, [to_list], fail_silently=False, html_message=html_message)
    return redirect('ReporteGanancias:debtors')
def addPay(request, pk):
    extra_forms = 1
    ParteFormSet = formset_factory(PresupuestosPagosForm, extra=extra_forms, max_num=20, can_delete=True)
    if request.method == 'POST':
        formset = ParteFormSet(request.POST, request.FILES, prefix='form')
        presupuesto = Presupuestos.objects.get(pk=pk)
        if formset.is_valid():
            for form in formset:
                if not form.cleaned_data["DELETE"]:
                    model_instance = form.save(commit=False)
                    model_instance.estimate = Presupuestos.objects.get(pk=pk)
                    presupuesto.total_paid += model_instance.cantidad_pagada
                    model_instance.save()
            presupuesto.save()
        request.session["messages"] = ["Payment is Added"]
        return redirect('ReporteGanancias:debtors')
    else:
        formset = ParteFormSet()
    return render(request, 'Presupuestos/estimate-add-payment.html', {
        'formset': formset,
    })



def addPart(request, pk):
    extra_forms = 1
    ParteFormSet = formset_factory(PresupuestosParteForm, extra=extra_forms, max_num=20, can_delete=True)
    presupuestos = Presupuestos.objects.filter(id=pk).values()[0]
    presupuestosForm = PresupuestosForm(initial=presupuestos)
    if request.method == 'POST':
        formset = ParteFormSet(request.POST, request.FILES, prefix='form')
        if formset.is_valid():
            for form in formset:
                if not form.cleaned_data["DELETE"]:
                    model_instance = form.save(commit=False)
                    model_instance.estimate_id = Presupuestos.objects.get(pk=pk)
                    model_instance.save()

            presupuestos = Presupuestos.objects.get(pk=pk)

            if (request.POST['descuento_parte'] == "Quantity"):
                presupuestos.descuentoTotal_parte += float(request.POST['descuentoTotal_parte'])
            elif(request.POST['descuento_parte'] == "Percentage"):
                presupuestos.descuentoTotal_parte += (100 - float(request.POST['descuentoTotal_parte'])) * float(request.POST['total_parte']) / float(request.POST['descuentoTotal_parte'])
            presupuestos.total_parte += float(request.POST['total_parte'])
            presupuestos.save()
            request.session["messages"] = ["part is Added"]
        return redirect('ReporteGanancias:debtors')
    else:
        formset = ParteFormSet()

    return render(request, 'Presupuestos/estimate-add-parts.html', {
        'presupuestosForm': presupuestosForm,
        'formset': formset,
    })



def addLabor(request, pk):
    extra_forms = 1
    ManoObraFormSet = formset_factory(PresupuestosManoObraForm, extra=extra_forms, max_num=20, can_delete=True)
    if request.method == 'POST':
        formset = ManoObraFormSet(request.POST, request.FILES, prefix='form')

        if formset.is_valid():
            for form in formset:
                if not form.cleaned_data["DELETE"]:
                    model_instance = form.save(commit=False)
                    model_instance.estimate_ids = Presupuestos.objects.get(pk=pk)
                    model_instance.save()
            presupuestos = Presupuestos.objects.get(pk=pk)

            if (request.POST['descuento_manaobra'] == "Quantity"):
                presupuestos.descuentoTotal_manaobra += float(request.POST['descuentoTotal_manaobra'])
            elif(request.POST['descuento_manaobra'] == "Percentage"):
                presupuestos.descuentoTotal_manaobra += (100 - float(request.POST['descuentoTotal_manaobra'])) * float(request.POST['total_manaobra'])/float(request.POST['descuentoTotal_manaobra'])
            presupuestos.total_manaobra += float(request.POST['total_manaobra'])
            presupuestos.save()
            request.session["messages"] = ["Labour is Added"]
        return redirect('ReporteGanancias:debtors')
    else:
        formset = ManoObraFormSet()
    return render(request, 'Presupuestos/estimate-add-labor.html', {
        'formset': formset,
    })


def pendingStock(request):

    if request.method == 'POST':
        fromdate=request.POST.get('fromdate')
        todate = request.POST.get('todate')
        searchresult = Parte.objects.filter(fecha_registro__range=(fromdate, todate))
        queryset = Parte.objects.filter(quantity__lt=10)
        return render(request,'ReporteGanancias/reports-pending-stock.html',{'parte':searchresult,'queryset':queryset})

    else:
        displaydata = Parte.objects.all()
    return render(request, 'ReporteGanancias/reports-pending-stock.html', {'parte': displaydata,'queryset':queryset})


class pendingStock(ListView):
    model=Parte
    template_name = 'ReporteGanancias/reports-pending-stock.html'
    context_object_name='parte'
    queryset = Parte.objects.filter(quantity__lt=10)


class Records(TemplateView):

    template_name = 'ReporteGanancias/reports-records.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['invoices'] = Invoices.objects.all()
        return context
def ViewInvoice(request,pk):
    invoice=Invoices.objects.get(pk=pk)
    presupuesto =  Presupuestos.objects.get(pk=invoice.estimate_id)
    print(Presupuestos.objects.values_list('carro_id').annotate(truck_count=Count('carro_id')).order_by('-truck_count'))
    return render(request,'ReporteGanancias/reports-invoice-detail.html',{'invoice':invoice,'presupuesto':presupuesto})
class Technicians(ListView):
    model=Presupuestos
    template_name = 'ReporteGanancias/reports-technicians.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        tech_estimates = []
        estimates = Presupuestos.objects.all()
        for estimate in estimates:
            for labour in estimate.manoobra_set.values():
                tech_estimates.append({
                    "presupuesto":estimate,
                    "labour":ManoObra.objects.get(pk=labour['id'])
                })

        context['estimates'] = tech_estimates
        return context
    # queryset=Presupuestos.objects.all()


class Workshops(ListView):
    model=ReporteGanancias
    template_name = 'ReporteGanancias/reports-workshops.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        carros = Presupuestos.objects.values_list('carro_id').annotate(truck_count=Count('carro_id')).order_by('-truck_count')[:10]
        cars=[]
        for carro in carros:
            if carro[0]==None:
                break
            cars.append(Carro.objects.get(pk=carro[0]))
        context['cars']=cars
        manoobras=ManoObra.objects.values_list('codigo').annotate(truck_count1=Count('id')).order_by('-truck_count1')[:10]
        labors=[]
        for manoobra in manoobras:
            labors.append(ManoObra.objects.filter(codigo=manoobra[0])[0])
        context['labors']=labors
        partes=Parte.objects.values_list('codigo').annotate(truck_count1=Count('id')).order_by('-truck_count1')[:10]
        parts=[]
        for part in partes:
            parts.append(Parte.objects.filter(codigo=part[0])[0])
        context['parts']=parts
        return context



class techniciansAddPayment(TemplateView):
    template_name='ReporteGanancias/reports-technicians-add-payment.html'

class techniciansViewPayment(TemplateView):
    template_name='ReporteGanancias/reports-technicians-view-payment.html'



 
