from datetime import datetime

from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView
from InformacionTiendas.models import InformacionTiendas
from Clientes.models import Clientes
from Presupuestos.models import Presupuestos
from invoices.models import Invoices


# class dashboard(TemplateView):
#
#     template_name = 'dashboard/dashboard.html'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         # Add in a QuerySet of all the books
#         context['workshop_count'] = InformacionTiendas.objects.count()
#         context['customer_count'] = Clientes.objects.count()
#         context['estimate_count'] = Presupuestos.objects.count()
#         invoices=Invoices.objects.all()
#         total_Revenu=0
#         for invoice in invoices:
#             total_Revenu+=invoice.amount
#         context['total_Revenu']=total_Revenu
#         return context
def dashboard(request):

    if request.method == 'POST':
        if request.POST['fromdate']:
            fromdate = request.POST.get('fromdate')
        else:
            fromdate ="2020-01-01"
        if request.POST['todate']:
            todate= request.POST.get('todate')
        else:
            todate = datetime.now
        workshop_count = InformacionTiendas.objects.count()
        customer_count = Clientes.objects.count()
        estimate_count = Presupuestos.objects.count()
        invoices = Invoices.objects.filter(date_register__range=(fromdate, todate))
        total_Revenu=0
        for invoice in invoices:
            total_Revenu+=invoice.amount
        return render(request,'dashboard/dashboard.html',{'workshop_count':workshop_count,'customer_count':customer_count,'estimate_count':estimate_count,'total_Revenu':total_Revenu})

    else:
        workshop_count = InformacionTiendas.objects.count()
        customer_count = Clientes.objects.count()
        estimate_count = Presupuestos.objects.count()
        invoices = Invoices.objects.all()
        total_Revenu = 0
        for invoice in invoices:
            total_Revenu += invoice.amount
    return render(request, 'dashboard/dashboard.html', {'workshop_count':workshop_count,'customer_count':customer_count,'estimate_count':estimate_count,'total_Revenu':total_Revenu})