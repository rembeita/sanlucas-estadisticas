# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin sqlcustom [app_label]'
# into your database.
from __future__ import unicode_literals

from django.db import models


class Camas(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    cama = models.CharField(db_column='Cama', max_length=20, blank=True, null=True)  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=20, blank=True, null=True)  # Field name made lowercase.
    asignable = models.CharField(db_column='Asignable', max_length=20, blank=True, null=True)  # Field name made lowercase.
    internac = models.IntegerField(db_column='Internac', blank=True, null=True)  # Field name made lowercase.
    ficha = models.IntegerField(db_column='Ficha', blank=True, null=True)  # Field name made lowercase.
    apellidoyn = models.CharField(db_column='Apellidoyn', max_length=200, blank=True, null=True)  # Field name made lowercase.
    nivel = models.CharField(db_column='Nivel', max_length=20, blank=True, null=True)  # Field name made lowercase.
    codigo = models.IntegerField(db_column='Codigo', blank=True, null=True)  # Field name made lowercase.
    estad = models.CharField(db_column='Estad', max_length=20, blank=True, null=True)  # Field name made lowercase.
    orden1 = models.IntegerField(db_column='Orden1', blank=True, null=True)  # Field name made lowercase.
    estado = models.CharField(db_column='Estado', max_length=20, blank=True, null=True)  # Field name made lowercase.
    usuario = models.CharField(db_column='Usuario', max_length=20, blank=True, null=True)  # Field name made lowercase.
    fechaproc = models.IntegerField(db_column='Fechaproc', blank=True, null=True)  # Field name made lowercase.
    horaproc = models.CharField(db_column='Horaproc', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CAMAS'
