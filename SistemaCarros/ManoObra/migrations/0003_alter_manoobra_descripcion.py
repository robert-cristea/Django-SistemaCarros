# Generated by Django 3.2.7 on 2021-10-25 16:59

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ManoObra', '0002_auto_20211025_1150'),
    ]

    operations = [
        migrations.AlterField(
            model_name='manoobra',
            name='descripcion',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]