from django.shortcuts import render
from django.views.generic import ListView

from invoices.models import Invoices
from tecnicos.models import Tecnicos

#
#
# def list_invoices(request):
#
#     if request.method == 'POST':
#         fromdate=request.POST.get('fromdate')
#         todate = request.POST.get('todate')
#         searchresult = Tecnicos.objects.filter(fecha_registro__range=(fromdate, todate))
#         return render(request,'invoices/list.html',{'tecnicos':searchresult})
#
#     else:
#         displaydata = Tecnicos.objects.all()
#     return render(request, 'invoices/list.html', {'tecnicos': displaydata})


#

class list_invoices(ListView):
    model=Invoices
    template_name = 'invoices/list.html'
    context_object_name='invoices'
    queryset=Tecnicos.objects.all()
