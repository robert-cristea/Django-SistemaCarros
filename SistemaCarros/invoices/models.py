from datetime import datetime

from django.db import models

# Create your models here.



class Invoices(models.Model):

    invoiceId= models.CharField(max_length=255,default=0)
    fechaInvoice=models.CharField(max_length=255,default=0)
    cuentaInvoice=models.IntegerField(default=0)
    cantidadInvoice=models.CharField(max_length=255,default=0)
    statusInvoice = models.CharField(max_length=255, default=0)
    fecha_registro = models.DateTimeField(default=datetime.now)


    def __str__(self):
        return f'{self.invoiceId} {self.fechaInvoice}{self.cuentaInvoice} {self.cantidadInvoice}' \
               f'{self.statusInvoice}{self.fecha_registro}'