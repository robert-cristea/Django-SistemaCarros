# Generated by Django 3.2.12 on 2022-03-31 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Parte', '0014_parte_estimate_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parte',
            name='descuento_parte',
            field=models.IntegerField(default=0),
        ),
    ]