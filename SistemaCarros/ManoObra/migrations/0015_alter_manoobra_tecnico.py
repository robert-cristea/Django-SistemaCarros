# Generated by Django 3.2.12 on 2022-04-08 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ManoObra', '0014_alter_manoobra_minutos'),
    ]

    operations = [
        migrations.AlterField(
            model_name='manoobra',
            name='tecnico',
            field=models.CharField(default='', max_length=200),
        ),
    ]
