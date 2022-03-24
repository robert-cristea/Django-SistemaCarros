from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView


class dashboard(TemplateView):
    template_name = 'dashboard/dashboard.html'