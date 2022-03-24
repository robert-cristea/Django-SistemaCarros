from . import views
from django.urls import path

app_name='Parte'

urlpatterns=[
    path('add',views.create_Parte,name='parte')
]