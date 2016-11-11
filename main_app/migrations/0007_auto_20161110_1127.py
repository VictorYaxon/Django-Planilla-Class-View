# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-10 17:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0006_auto_20161110_1126'),
    ]

    operations = [
        migrations.AlterField(
            model_name='igss',
            name='anio',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='igss',
            name='cuota_igss',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='planilla',
            name='anio',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='planilla',
            name='mes',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='planillagenerar',
            name='bonificacion_planilla',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='planillagenerar',
            name='cuota_salario_planilla',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='planillagenerar',
            name='igss_anio_planilla',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='planillagenerar',
            name='igss_cuota',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='planillagenerar',
            name='mes_planilla',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='planillagenerar',
            name='retencion_planilla',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='planillagenerar',
            name='sueldoLiquido_planilla',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='planillagenerar',
            name='sueldoTotal_planilla',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='salarioordinario',
            name='anio',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='salarioordinario',
            name='cuota_salario',
            field=models.FloatField(),
        ),
    ]
