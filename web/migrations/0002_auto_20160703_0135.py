# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='persona',
            name='ubicaciones',
            field=models.ManyToManyField(to='web.Ubicacion', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='persona',
            name='zonas',
            field=models.ManyToManyField(to='web.Zona', null=True, blank=True),
        ),
    ]
