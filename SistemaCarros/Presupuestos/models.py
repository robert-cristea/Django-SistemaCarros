from django.db import models

# Create your models here.
from Clientes.models import Clientes
from carros.models import Carro
from tecnicos.models import Tecnicos
from Foto.models import Foto

class Presupuestos(models.Model):
    cliente= models.ForeignKey(Clientes, on_delete=models.SET_NULL, null=True)
    carro=models.ForeignKey(Carro, on_delete=models.SET_NULL, null=True)
    #mano_obra=models.ForeignKey(ManoObra, on_delete=models.SET_NULL, null=True)
    #parte=models.ForeignKey(Parte, on_delete=models.SET_NULL, null=True)
    garantia=models.CharField(max_length=255,default=0)
    #pago = models.ForeignKey(Pagos, on_delete=models.SET_NULL, null=True)
    foto = models.ForeignKey(Foto, on_delete=models.SET_NULL, null=True)
    tecnicos=models.ForeignKey(Tecnicos, on_delete=models.SET_NULL, null=True)
    descuento_parte=models.CharField(max_length=255,default="0")
    total_parte=models.IntegerField(null=True,blank=True)
    descuentoTotal_parte= models.IntegerField(null=True,blank=True)
    descuento_manaobra=models.CharField(max_length=255,default="0")
    total_manaobra=models.IntegerField(null=True,blank=True)
    descuentoTotal_manaobra= models.IntegerField(null=True,blank=True)
    resumen=models.CharField(max_length=255,blank=True)
    register_time=models.CharField(max_length=255,blank=True)

    @property
    def total(self):
        return self.total_manaobra+self.total_parte
    #detalle=models.ForeignKey(Detalle, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f'{self.cliente} {self.carro}{self.garantia}' \
               f'{self.tecnicos}'\
               f'{self.descuento_parte} {self.descuentoTotal_parte} {self.total_parte}'\
               f'{self.descuento_manaobra} {self.descuentoTotal_manaobra} {self.total_manaobra}'

