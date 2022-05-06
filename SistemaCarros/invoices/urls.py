from . import views
from django.urls import path
from django.contrib.auth.decorators import login_required
app_name='invoices'

urlpatterns=[
    path('',login_required(views.list_invoices.as_view()),name='list'),
]