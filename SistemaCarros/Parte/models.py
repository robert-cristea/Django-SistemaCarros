from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.


class Parte(models.Model):

    resumen = models.TextField()
    codigo=models.IntegerField()
    descripcion=models.CharField(max_length=255,blank=True, null=True)
    quantity=models.IntegerField()
    unit_price=models.IntegerField()
    descuento=models.CharField(max_length=255,default="0")
    total_price=models.IntegerField()
    tax_free=models.BooleanField()
    descuentoTotal= models.IntegerField()
    descuento_parte = models.IntegerField()
    comprado_cliente=models.BooleanField(default='0')
    total=models.IntegerField()

    # estatus = models.BooleanField()
    # def __str__(self):
    #     return f'{self.codigo}: {self.estatus} {s
    #     elf.descripcion}'




    def __str__(self):
        return f'{self.codigo}: {self.descripcion} {self.quantity} {self.unit_price} {self.total_price}' \
               f' {self.tax_free}{self.descuento}{self.descuentoTotal}{self.descuento_parte}{self.total}' \
               f'{self.comprado_cliente}{self.resumen}'