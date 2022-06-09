from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template import loader
from django.urls import reverse_lazy
from django.views.generic import ListView
from django_xhtml2pdf.utils import generate_pdf
from django.views.generic import TemplateView, UpdateView, CreateView, DeleteView, DetailView
from Presupuestos.models import Presupuestos
from invoices.models import Invoices
from tecnicos.models import Tecnicos


class list_invoices(ListView):
    model=Invoices
    template_name = 'invoices/list.html'
    context_object_name='invoices'
    queryset=Invoices.objects.all()

def detail_invoices(request, pk):
    invoice = Invoices.objects.get(pk=pk)
    presupuesto=Presupuestos.objects.get(pk=invoice.estimate_id)
    if request.method == 'POST':
        html_message = loader.render_to_string(
            'invoices/invoice-pdf.html',
            {'presupuesto': presupuesto}
        )
        email_subject = 'Your Updated Estimate!'
        to_list = 'customer@dinh.mail.com'
        send_mail(email_subject, 'message', None, [to_list], fail_silently=False, html_message=html_message)
        request.session["messages"] = ["Updated Estimate is sent by Email"]
        return redirect('Invoices:list')
    else:
        return render(request, "invoices/invoice-detail.html",
                  {'presupuesto': presupuesto})
def download_pdf(request,pk):
    invoice=Invoices.objects.get(pk=pk)
    presupuesto = Presupuestos.objects.get(pk=invoice.estimate_id)
    context = {'presupuesto': presupuesto}
    result = generate_pdf('Presupuestos/estimate-pdf.html',context=context)

    response = HttpResponse(result.getvalue(), content_type='application/pdf')
    filename = "Invoice_%s.pdf" % pk
    content = "attachment; filename=%s" % filename
    response['Content-Disposition'] = content
    return response
class delete_invoice(DeleteView):
    model = Invoices
    success_url=reverse_lazy('invoices:list')
