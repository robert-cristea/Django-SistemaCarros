from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.





class ManoObra(models.Model):

    OPERATOR = (
        ('Operator 1', 'Operator 1'),
        ('Operator 2', 'Operator 2'),
        ('Operator 3', 'Operator 3'),

    )


    codigo=models.IntegerField()
    descripcion=models.TextField(blank=True,default=0)
    tecnico=models.CharField(max_length=200, choices=OPERATOR,default='Operator ')
    horas=models.IntegerField()
    minutos=models.IntegerField()
    tarifa=models.IntegerField()
    tarifa_total = models.IntegerField()
    libre_impuestos=models.BooleanField()
    descuento=models.CharField(max_length=255)
    numeroDescuento=models.IntegerField()
    total = models.IntegerField()

    tarifa_hora=models.IntegerField(null=True)


    def __str__(self):
        return f'{self.codigo} {self.tecnico} {self.tarifa_hora} {self.horas}{self.minutos} {self.tarifa}' \
               f'{self.libre_impuestos}{self.descuento}{self.tarifa_total}{self.descripcion}{self.total}' \
               f'{self.numeroDescuento}'
