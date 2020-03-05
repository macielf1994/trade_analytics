# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Acoes(models.Model):
    class Meta:
        verbose_name_plural = 'Ações'

class ETFs(models.Model):
    class Meta:
        verbose_name_plural = "ETF's"

class RendaFixa(models.Model):
    class Meta:
        verbose_name_plural = 'Renda Fixa'

