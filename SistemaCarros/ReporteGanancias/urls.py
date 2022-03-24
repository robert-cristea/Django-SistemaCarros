from . import views
from django.urls import path

app_name='ReporteGanancias'

urlpatterns=[
    path('',views.IndexReporteGanancias.as_view(),name='reporteganancias'),
    path('reports-debtors', views.reportsDebtors.as_view(), name='debtors'),
    path('reports-pending-stock', views.pendingStock.as_view(), name='pending-stock'),
    path('reports-records', views.Records.as_view(), name='records'),
    path('reports-technicians', views.Technicians.as_view(), name='technicians'),
    path('reports-workshops', views.Workshops.as_view(), name='workshops'),
    # path('edit/<int:pk>', views.edit_inventory.as_view(), name='edit_tecnicos'),
    # path('edit',views.addPart.as_view(),name='add-part'),
]