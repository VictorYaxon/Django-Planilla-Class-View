# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-10 18:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0008_auto_20161110_1241'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empleado',
            name='fechaInactividad',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
