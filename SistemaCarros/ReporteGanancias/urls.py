from . import views
from django.urls import path


app_name='ReporteGanancias'

urlpatterns=[
    path('',views.IndexReporteGanancias.as_view(),name='reporteganancias'),
    path('reports-debtors', views.reportsDebtors, name='debtors'),
    path('reports-pending-stock', views.pendingStock.as_view(), name='pending-stock'),
    path('reports-records', views.Records.as_view(), name='records'),
    path('reports-technicians', views.Technicians.as_view(), name='technicians'),
    path('reports-workshops', views.Workshops, name='workshops'),
    path('reports-technicians-add-payment', views.techniciansAddPayment.as_view(), name='techniciansAddPayment'),
    path('reports-technicians-view-payment', views.techniciansViewPayment.as_view(), name='techniciansViewPayment'),
    path('send-email/<int:pk>', views.send_email, name='send-email'),
    path('add-pay/<int:pk>',views.addPay,name='add-pay'),
    path('add-part/<int:pk>',views.addPart,name='add-part'),
    path('add-labor/<int:pk>',views.addLabor,name='add-labor'),
    path('detail-invoice/<int:pk>',views.ViewInvoice,name='detail-invoice'),
    # path('edit/<int:pk>', views.edit_inventory.as_view(), name='edit_tecnicos'),
    # path('edit',views.addPart.as_view(),name='add-part'),
] 
