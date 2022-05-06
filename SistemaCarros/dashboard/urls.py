from . import views
from django.urls import path
from django.contrib.auth.decorators import login_required
app_name='dashboard'

urlpatterns=[
    #/dashboard/
    path('',login_required(views.dashboard.as_view()),name='dashboard'),

]