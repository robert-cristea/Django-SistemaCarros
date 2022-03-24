from . import views
from django.urls import path

app_name='dashboard'

urlpatterns=[
    #/dashboard/
    path('',views.dashboard.as_view(),name='dashboard'),

]