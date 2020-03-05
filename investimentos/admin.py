# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Acoes
from .models import ETFs
from .models import RendaFixa

@admin.register(Acoes)

class AcoesAdmin(admin.ModelAdmin):
    list_display = []

@admin.register(ETFs)

class ETFsAdmin(admin.ModelAdmin):
    list_display = []

@admin.register(RendaFixa)

class RendaFixaAdmin(admin.ModelAdmin):
    list_display = []
