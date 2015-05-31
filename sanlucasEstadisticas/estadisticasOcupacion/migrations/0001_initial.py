# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Camas',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cama', models.CharField(max_length=20, null=True, db_column='Cama', blank=True)),
                ('descripcion', models.CharField(max_length=20, null=True, db_column='Descripcion', blank=True)),
                ('asignable', models.CharField(max_length=20, null=True, db_column='Asignable', blank=True)),
                ('internac', models.IntegerField(null=True, db_column='Internac', blank=True)),
                ('ficha', models.IntegerField(null=True, db_column='Ficha', blank=True)),
                ('apellidoyn', models.CharField(max_length=200, null=True, db_column='Apellidoyn', blank=True)),
                ('nivel', models.CharField(max_length=20, null=True, db_column='Nivel', blank=True)),
                ('codigo', models.IntegerField(null=True, db_column='Codigo', blank=True)),
                ('estad', models.CharField(max_length=20, null=True, db_column='Estad', blank=True)),
                ('orden1', models.IntegerField(null=True, db_column='Orden1', blank=True)),
                ('estado', models.CharField(max_length=20, null=True, db_column='Estado', blank=True)),
                ('usuario', models.CharField(max_length=20, null=True, db_column='Usuario', blank=True)),
                ('fechaproc', models.IntegerField(null=True, db_column='Fechaproc', blank=True)),
                ('horaproc', models.CharField(max_length=20, null=True, db_column='Horaproc', blank=True)),
            ],
            options={
                'db_table': 'CAMAS',
                'managed': False,
            },
        ),
    ]
