from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView
from InformacionTiendas.models import InformacionTiendas
from Clientes.models import Clientes
from Presupuestos.models import Presupuestos
class dashboard(TemplateView):

    template_name = 'dashboard/dashboard.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['workshop_count'] = InformacionTiendas.objects.count()
        context['customer_count'] = Clientes.objects.count()
        context['estimate_count'] = Presupuestos.objects.count()
        return context

