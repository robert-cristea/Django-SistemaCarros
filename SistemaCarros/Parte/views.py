from django.forms import formset_factory
from django.shortcuts import render, redirect

# Create your views here.
from .forms import ParteForm


def create_Parte(request):
    form=ParteForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('parte:index')
    return render(request,'Parte/parte-form.html',{'form':form})



