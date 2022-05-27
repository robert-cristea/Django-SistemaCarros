import datetime

from django.forms import formset_factory, modelform_factory
from django.http import HttpResponseRedirect, HttpResponse, FileResponse
from django.template import loader
from django.views.generic import TemplateView

from Clientes.models import Clientes
from ManoObra.models import ManoObra
from Parte.models import Parte
from carros.models import Carro
from Pagos.models import Pagos
from invoices.models import Invoices
from tecnicos.models import Tecnicos
from .forms import PresupuestosClientesForm, PresupuestosVehiculosForm, PresupuestosParteForm, PresupuestosManoObraForm, \
    PresupuestosPagosForm, PresupuestosForm
 #Create your views here.
from .models import Presupuestos
from django.shortcuts import render, redirect
from django_xhtml2pdf.utils import generate_pdf
from django.core.mail import send_mail
# Create your views here.




def step1(request):
    clientes=Clientes.objects.all()
    presupuestosclientesform = PresupuestosClientesForm(request.POST or None)
    if request.method == 'POST':
        if presupuestosclientesform.is_valid():
            flag=0
            for cliente in clientes:
                if cliente.correo==presupuestosclientesform.cleaned_data['correo']:
                    flag=1
                    break
            if flag==0:
               presupuestosclientesform.save()
               current_customer=Clientes.objects.all.last()
            else:
                current_customer=Clientes.objects.filter(correo=presupuestosclientesform.cleaned_data['correo'])[0]
            presupuesto_instance=Presupuestos()
            presupuesto_instance.cliente_id=current_customer.id
            presupuesto_instance.save()
            request.session['client_id']=current_customer.id
            return redirect('Presupuestos:step2')
    else:
        presupuestosclientesform = PresupuestosClientesForm(request.POST or None)

    return render(request,'Presupuestos/new-estimate-1-customer-details.html',{
        'presupuestosclientesform':presupuestosclientesform,

    })




def step2(request):
    cars=Carro.objects.all()
    presupuestosvehiculosform=PresupuestosVehiculosForm(request.POST or None)
    if request.method == 'POST':
        if presupuestosvehiculosform.is_valid():
            flag = 0
            for car in cars:
                if car.modelo == presupuestosvehiculosform.cleaned_data['modelo'] and car.placas==presupuestosvehiculosform.cleaned_data['placas']:
                    flag = 1
                    break
            if flag == 0:
                presupuestosvehiculosform.save()
                current_car = Carro.objects.all.last()
            else:
                current_car = Carro.objects.filter(modelo=presupuestosvehiculosform.cleaned_data['modelo'])[0]
            presupuesto_instance = Presupuestos.objects.all().last()
            presupuesto_instance.cliente_id = current_car.id
            presupuesto_instance.save()
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
    ParteFormSet = formset_factory(PresupuestosParteForm, extra=extra_forms, max_num=20,can_delete=True)
    if request.method == 'POST':
        request.session['resumen'] = request.POST['resumen']
        presupuestos_instance = Presupuestos()
        presupuestos_instance.resumen=request.POST['resumen']
        presupuestos_instance.save()
        request.session['descuento_parte'] = request.POST['descuento_parte']
        request.session['descuentoTotal_parte'] = request.POST['descuentoTotal_parte']
        request.session['total_parte'] = request.POST['total_parte']
        formset = ParteFormSet(request.POST, request.FILES, prefix='form')
        if formset.is_valid():
            for form in formset:
                # if not form.cleaned_data["DELETE"]:
                    model_instance = form.save(commit=False)
                    model_instance.estimate_id = Presupuestos.objects.all().last()
                    model_instance.save()
            return redirect('Presupuestos:step4')
    else:
        formset = ParteFormSet()

    return render(request, 'Presupuestos/new-estimate-3-parts.html', {
        'formset': formset,
    })

def step4(request):
    extra_forms = 1
    ManoObraFormSet = formset_factory(PresupuestosManoObraForm, extra=extra_forms, max_num=20, can_delete=True)
    if request.method == 'POST':
        request.session['total_manaobra']=request.POST['total_manaobra']
        formset = ManoObraFormSet(request.POST, request.FILES, prefix='form')

        if formset.is_valid():
            for form in formset:
                if not form.cleaned_data["DELETE"]:
                    model_instance = form.save(commit=False)
                    model_instance.estimate_ids = Presupuestos.objects.all().last()
                    model_instance.save()
            return redirect('Presupuestos:step5')
    else:
        manoobra_formset = ManoObraFormSet()
    return render(request, 'Presupuestos/new-estimate-4-labor.html', {
        'formset': manoobra_formset,

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
    ParteFormSet = formset_factory(PresupuestosPagosForm, extra=extra_forms, max_num=20, can_delete=True)
    if request.method == 'POST':
        formset = ParteFormSet(request.POST, request.FILES, prefix='form')
        if formset.is_valid():
            current_presupuesto = Presupuestos.objects.all().last()
            for form in formset:
                if not form.cleaned_data["DELETE"]:
                    model_instance = form.save(commit=False)
                    model_instance.estimate = current_presupuesto
                    current_presupuesto.total_paid += model_instance.cantidad_pagada
                    model_instance.save()
            current_presupuesto.save()
            return redirect('Presupuestos:step7')
    else:
        formset = ParteFormSet(prefix='form')


    return render(request,'Presupuestos/new-estimate-6-payments.html',{
        'formset':formset
    })


#
def step7(request):
    step_estimate=Presupuestos.objects.all().last()
    technicans = Tecnicos.objects.all()
    step_client = Clientes.objects.get(pk=request.session['client_id'])
    step_vehicle = Carro.objects.get(pk=request.session['car_id'])
    step_parte=Parte.objects.filter(estimate_id=step_estimate.id)
    step_manoobra=ManoObra.objects.filter(estimate_ids=step_estimate.id)
    step_pago=Pagos.objects.filter(estimate_id=step_estimate.id)
    payment = 0
    for step in step_pago:
        payment += step.cantidad_pagada
    total = float(request.session['total_parte']) + float(request.session['total_manaobra'])
    balance = step_estimate.total-step_estimate.total_paid
    if request.method=='POST':
        #create completed estimate
        presupuestos=Presupuestos.objects.all().last()
        presupuestos.total_parte=float(request.session['total_parte'])
        presupuestos.total_manaobra=float(request.session['total_manaobra'])
        # presupuestos.descuento_parte=request.session['descuento_parte']
        presupuestos.descuentoTotal_parte=float(request.session['descuentoTotal_parte'])
        presupuestos.descuentoTotal_manaobra=float(request.session['descuentoTotal_manaobra'])

        presupuestos.cliente_id=request.session['client_id']
        presupuestos.carro_id=request.session['car_id']
        presupuestos.tecnicos_id=request.POST['technican_select']
        #create invoice related to estimate
        if presupuestos.total_paid==presupuestos.total:
            presupuestos.status="paid"
            invoice_instance = Invoices()
            invoice_instance.estimate = presupuestos.id
            invoice_instance.amount = presupuestos.total
            invoice_instance.status = presupuestos.status
            invoice_instance.save()
        presupuestos.save()
        return redirect('Presupuestos:step8')
    else:
        return render(request, 'Presupuestos/new-estimate-7-preview.html',
                  {'technicans': technicans, 'step_client': step_client, 'step_vehicle': step_vehicle,
                   'step_parte': step_parte, 'step_manoobra': step_manoobra, 'balance': balance, 'total': total,'step_estimate':step_estimate})


class step8(TemplateView):
    template_name='Presupuestos/new-estimate-8-confirm.html'



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
        return redirect('Presupuestos:presupuestos')
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
        return redirect('Presupuestos:presupuestos')
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
        return redirect('Presupuestos:presupuestos')
    else:
        formset = ManoObraFormSet()
    return render(request, 'Presupuestos/estimate-add-labor.html', {
        'formset': formset,
    })


def presupuestosIndex(request):
    presupuestos_all = Presupuestos.objects.all()
    send_data = {'presupuestos': presupuestos_all}

    if request.session.get("messages"):
        send_data = {
            'presupuestos': presupuestos_all,
            'messages':request.session.get("messages")
        }
        request.session.pop("messages")

    return render(request, "Presupuestos/presupuestos.html",
                      send_data)


def detail_presupuestos(request, pk):
    presupuesto = Presupuestos.objects.get(pk=pk)
    if request.method == 'POST':
        html_message = loader.render_to_string(
            'Presupuestos/estimate-pdf.html',
            {'presupuesto': presupuesto}
        )
        email_subject = 'Your Updated Estimate!'
        to_list = 'customer@dinh.mail.com'
        send_mail(email_subject, 'message', None, [to_list], fail_silently=False, html_message=html_message)
        request.session["messages"] = ["Updated Estimate is sent by Email"]
        return redirect('Presupuestos:presupuestos')
    else:
        return render(request, "Presupuestos/presupuestos-detail.html",
                  {'presupuesto': presupuesto})
def send_email(request,pk):
    presupuesto = Presupuestos.objects.get(pk=pk)
    html_message = loader.render_to_string(
        'Presupuestos/estimate-pdf.html',
        {'presupuesto': presupuesto}
    )
    email_subject = 'Your Estimate!'
    to_list = 'customer@dinh.mail.com'
    send_mail(email_subject, 'message', None, [to_list], fail_silently=False, html_message=html_message)
    return render(request,"ReporteGanacias/reports-debtors.html")

def detail_in_pdf(request, pk):
    presupuesto = Presupuestos.objects.get(pk=pk)
    return render(request,"Presupuestos/estimate-pdf.html",{'presupuesto':presupuesto})

def cancel_presupuestos(request, pk):
    presupuesto = Presupuestos.objects.get(pk=pk)
    presupuesto.status = "canceled"
    presupuesto.save()
    request.session["messages"] = ["Estimate is canceled"]
    return redirect('Presupuestos:presupuestos')
def download_pdf(request,pk):
    # presupuesto = Presupuestos.objects.get(pk=pk)
    # return render(request, 'Presupuestos/estimate-pdf.html',{'presupuesto':presupuesto})
    presupuesto = Presupuestos.objects.get(pk=pk)
    context = {'presupuesto': presupuesto}
    result = generate_pdf('Presupuestos/estimate-pdf.html',context=context)

    response = HttpResponse(result.getvalue(), content_type='application/pdf')
    filename = "Estimate_%s.pdf" % pk
    content = "attachment; filename=%s" % filename
    response['Content-Disposition'] = content
    return response

