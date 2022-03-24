from . import views
from django.urls import path

app_name='Presupuestos'

urlpatterns=[
    # path('new-customer',views.create_Presupuestos,name='nuevo-presupuestos'),
    path('step1',views.step1,name='step1'),
    path('step2',views.step2,name='step2'),
    path('step3',views.step3,name='step3'),
    path('step4',views.step4,name='step4'),
    path('step5',views.step5,name='step5'),
    path('step6',views.step6,name='step6'),
    path('step7/',views.step7,name='step7'),
    path('step8',views.step8.as_view(),name='step8'),
    path('',views.presupuestosIndex.as_view(),name='presupuestos'),
    path('add-pay',views.addPay.as_view(),name='add-pay'),
    path('add-part',views.addPart.as_view(),name='add-part'),
    path('add-labor',views.addLabor.as_view(),name='add-labor'),
]