from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView

from inventory.models import Inventory
from .forms import ReporteGananciasForm
from carros.models import Carro
from ManoObra.models import ManoObra
from Presupuestos.models import Presupuestos
# Create your views here.
from .models import ReporteGanancias


class IndexReporteGanancias(TemplateView):
    template_name='ReporteGanancias/list.html'


class reportsDebtors(ListView):
    model=Presupuestos
    template_name = 'ReporteGanancias/reports-debtors.html'
    context_object_name='debtors'
    queryset=Presupuestos.objects.all()


class pendingStock(ListView):
    model=Inventory
    template_name = 'ReporteGanancias/reports-pending-stock.html'
    context_object_name='inventory'
    queryset = Inventory.objects.filter(quantityInventory__lt=10)


class Records(ListView):
    model=ReporteGanancias
    template_name = 'ReporteGanancias/reports-records.html'
    # context_object_name='records'
    queryset=ReporteGanancias.objects.all()

class Technicians(ListView):
    model=ReporteGanancias
    template_name = 'ReporteGanancias/reports-technicians.html'
    # context_object_name='technicians'
    queryset=ReporteGanancias.objects.all()


class Workshops(TemplateView):
    template_name = 'ReporteGanancias/reports-workshops.html'
    # context_object_name='workshops'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['top_vehicles'] = Carro.objects.values('marca', 'modelo', 'tipo', 'año')[:10]
        context['top_labors'] = ManoObra.objects.all()[:10]
        return context;

