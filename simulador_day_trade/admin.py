# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Operacoes
from .models import SimuladorDeStops

@admin.register(Operacoes)

class OperacoesAdmin(admin.ModelAdmin):
    list_display = [
        'data',
        'horario_de_abertura', 
        'horario_de_fechamento',
        'categoria',
        'corretora',
        'corretagem',
        'custos_b3',
        'ativo',
        'sizing',
        'direcao',
        'contexto',
        'estrategia',
        'distancia_media',
        'tempo_grafico_entrada',
        'tempo_grafico_correlacionado',
        'risco_incial',
        'resultado_operacional',
        'comentarios_adicionais',
        ]

@admin.register(SimuladorDeStops)

class SimuladorDeStopsAdmin(admin.ModelAdmin):
    list_display = [
        'stop_primeiro_teste',
        'stop_segundo_teste',
        'stop_terceiro_teste',
        'stop_quarto_teste',
        'stop_quinto_teste'
        ]