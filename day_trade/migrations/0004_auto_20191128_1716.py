# -*- coding: utf-8 -*-
# Generated by Django 1.11.26 on 2019-11-28 20:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('day_trade', '0003_auto_20191128_1549'),
    ]

    operations = [
        migrations.AlterField(
            model_name='operacoes',
            name='estrategia',
            field=models.CharField(default='H/L2', max_length=30, verbose_name='Estrat\xe9gia*:'),
        ),
    ]
