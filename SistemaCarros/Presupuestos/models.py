from django.db import models

# Create your models here.
from Clientes.models import Clientes
from carros.models import Carro
from tecnicos.models import Tecnicos


class Presupuestos(models.Model):
    PRESUPUESTO_STATUS = (
        ('PENDING', 'pending'),
        ('CANCELED', 'canceled'),
    )
    cliente= models.ForeignKey(Clientes, on_delete=models.SET_NULL, null=True)
    carro=models.ForeignKey(Carro, on_delete=models.SET_NULL, null=True)
    # mano_obra=models.ForeignKey(ManoObra, on_delete=models.SET_NULL, null=True)
    # parte=models.ForeignKey(Parte, on_delete=models.SET_NULL, null=True)
    garantia=models.CharField(max_length=255,default=0)
    # pago = models.ForeignKey(Pagos, on_delete=models.SET_NULL, null=True)
    # foto = models.ForeignKey(Foto, on_delete=models.SET_NULL, null=True)
    tecnicos=models.ForeignKey(Tecnicos, on_delete=models.SET_NULL, null=True)
    #descuento_parte=models.CharField(max_length=255,default="0")
    total_parte=models.FloatField(null=True,blank=True)
    descuentoTotal_parte= models.FloatField(null=True,blank=True)
    #descuento_manaobra=models.CharField(max_length=255,default="0")
    total_manaobra=models.FloatField(null=True,blank=True)
    descuentoTotal_manaobra= models.FloatField(null=True,blank=True)
    total_paid = models.FloatField(default=0, blank=True, null=True)
    status = models.CharField(choices=PRESUPUESTO_STATUS,default="PENDING", max_length=10)
    resumen=models.CharField(max_length=255,blank=True)
    register_time=models.DateTimeField(auto_now=True)

    @property
    def total(self):
        return self.total_manaobra+self.total_parte
    #detalle=models.ForeignKey(Detalle, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f'{self.cliente} {self.carro}{self.garantia}' \
               f'{self.tecnicos}'\
               f'{self.descuentoTotal_parte} {self.total_parte}'\
               f' {self.descuentoTotal_manaobra} {self.total_manaobra}'



