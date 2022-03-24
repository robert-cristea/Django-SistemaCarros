import json
import os

from django.contrib.messages.views import SuccessMessageMixin
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.views.generic import TemplateView, UpdateView, CreateView, DeleteView, DetailView
from django.views.generic.list import ListView

from django.shortcuts import render, redirect

# Create your views here.
from SistemaCarros import settings
from carros.forms import CarroForm
from carros.models import Carro
from django.core.files.storage import default_storage, FileSystemStorage


class IndexClassView(ListView):
    model=Carro
    template_name = 'carros/index.html'
    context_object_name='carros'
    queryset=Carro.objects.all()


def list_cars(request):

    if request.method == 'POST':
        fromdate = request.POST.get('fromdate')
        todate = request.POST.get('todate')
        searchresult = Carro.objects.filter(fecha_registros__range=(fromdate, todate))
        return render(request,'carros/index.html',{'carros':searchresult})

    else:
        displaydata = Carro.objects.all()
    return render(request, 'carros/index.html', {'carros': displaydata})

def Imagedetail(request):
    car_id = request.POST.get('id')
    current_car = Carro.objects.get(id=car_id)
    return JsonResponse(json.dumps(list(json.loads(current_car.fotosCarro).keys())), safe=False)


class detail_carro(DetailView):
    template_name = 'carros/carros-detail.html'
    queryset=Carro.objects.all()
    context_object_name = 'carros'



class EditClassView(UpdateView):
    model = Carro
    template_name= 'carros/carros-form-add.html'
    form_class=CarroForm
    success_url = reverse_lazy('carros:list_cars')


#
class create_carros(SuccessMessageMixin,CreateView):
    model=Carro
    form_class=CarroForm
    template_name='carros/carros-form-add.html'
    success_url=reverse_lazy('carros:list_cars')
    success_message = "%(modelo)s this is was created successfully"


#
def create_carros_picture(request):

        if request.FILES['files']:
            file = request.FILES['files']
            fs = FileSystemStorage()  # defaults to   MEDIA_ROOT
            new_name = "tome"
            new_name = fs.get_valid_name(new_name)+".jpg"
            filename = fs.save(new_name, file)
            return JsonResponse({filename:file.name},safe=False)
        else:
            form=CarroForm()
            return render(request, "carros/carros-form-add.html",{'form':form})


def create_carros_warranty(request):
    if request.FILES['files']:
        file = request.FILES['files']
        fs = FileSystemStorage()  # defaults to   MEDIA_ROOT
        new_name = "warranty"
        new_name = fs.get_valid_name(new_name) + ".jpg"
        filename = fs.save(new_name, file)
        return JsonResponse({filename: file.name}, safe=False)
    else:
        form = CarroForm()
        return render(request, "carros/carros-form-add.html", {'form': form})


class delete_carro(DeleteView):
    model = Carro
    success_url=reverse_lazy('carros:list_cars')




