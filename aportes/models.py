# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Aportes(models.Model):
    class Meta:
        verbose_name_plural = 'Aportes'

    data_aporte = models.DateField(
        'Data do aporte:',
        blank=True,
        null=True
    )

    aportes = models.DecimalField(
        'Valor do aporte:',
        max_digits=50,
        decimal_places=2,
        blank=True,
        null=True
    )

