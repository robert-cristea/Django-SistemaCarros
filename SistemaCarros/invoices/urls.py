from . import views
from django.urls import path

app_name='invoices'

urlpatterns=[
    path('',views.list_invoices.as_view(),name='list'),
]