# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_auto_20160703_0135'),
    ]

    operations = [
        migrations.AlterField(
            model_name='persona',
            name='apellido',
            field=models.CharField(max_length=500, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='persona',
            name='dni',
            field=models.CharField(max_length=500, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='persona',
            name='fecha_de_nacimiento',
            field=models.DateTimeField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='persona',
            name='nombre',
            field=models.CharField(max_length=500, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='tramite',
            name='descripcion',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='tramite',
            name='fecha_de_inicio',
            field=models.DateTimeField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='tramite',
            name='nombre',
            field=models.CharField(max_length=500, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='tramite',
            name='persona',
            field=models.ForeignKey(blank=True, to='web.Persona', null=True),
        ),
        migrations.AlterField(
            model_name='ubicacion',
            name='calle_1',
            field=models.CharField(max_length=500, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='ubicacion',
            name='calle_2',
            field=models.CharField(max_length=500, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='ubicacion',
            name='calle_3',
            field=models.CharField(max_length=500, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='zona',
            name='nombre',
            field=models.CharField(max_length=500, null=True, blank=True),
        ),
    ]
