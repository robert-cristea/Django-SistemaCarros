from django.db import models

# Create your models here.
from Clientes.models import Clientes
from Foto.models import Foto
from ManoObra.models import ManoObra
from Pagos.models import Pagos
from Parte.models import Parte
from carros.models import Carro
from tecnicos.models import Tecnicos


class Presupuestos(models.Model):
    cliente= models.ForeignKey(Clientes, on_delete=models.SET_NULL, null=True)
    carro=models.ForeignKey(Carro, on_delete=models.SET_NULL, null=True)
    mano_obra=models.ForeignKey(ManoObra, on_delete=models.SET_NULL, null=True)
    parte=models.ForeignKey(Parte, on_delete=models.SET_NULL, null=True)
    garantia=models.CharField(max_length=255,default=0)
    pago = models.ForeignKey(Pagos, on_delete=models.SET_NULL, null=True)
    foto = models.ForeignKey(Foto, on_delete=models.SET_NULL, null=True)
    tecnicos=models.ForeignKey(Tecnicos, on_delete=models.SET_NULL, null=True)

    #detalle=models.ForeignKey(Detalle, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f'{self.cliente} {self.carro}{self.mano_obra} {self.parte}{self.garantia}' \
               f'{self.pago}{self.foto}{self.tecnicos}'

