# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=500)),
                ('apellido', models.CharField(max_length=500)),
                ('dni', models.CharField(max_length=500)),
                ('fecha_de_nacimiento', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Tramite',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha_de_inicio', models.DateTimeField()),
                ('nombre', models.CharField(max_length=500)),
                ('descripcion', models.TextField()),
                ('persona', models.ForeignKey(to='web.Persona')),
            ],
        ),
        migrations.CreateModel(
            name='Ubicacion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('calle_1', models.CharField(max_length=500)),
                ('calle_2', models.CharField(max_length=500)),
                ('calle_3', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Zona',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=500)),
            ],
        ),
        migrations.AddField(
            model_name='persona',
            name='ubicaciones',
            field=models.ManyToManyField(to='web.Ubicacion'),
        ),
        migrations.AddField(
            model_name='persona',
            name='zonas',
            field=models.ManyToManyField(to='web.Zona'),
        ),
    ]
