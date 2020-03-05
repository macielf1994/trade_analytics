from __future__ import unicode_literals

from django.contrib import admin
from .models import Operacoes

@admin.register(Operacoes)

class OperacoesAdmin(admin.ModelAdmin):
    list_display = [
        'data_abertura',
        'data_fechamento',
        'vencimento_das_opcoes',
        'nivel_vol_implicita',
        'serie_vencimento_opcoes',
        'ticker_ativo_subjacente',
        'motivo_da_operacao',
        'timeframe_do_grafico',
        'estrategia_de_alta',
        'estrategia_de_baixa',
        'estrategia_de_lateralidade',
        'contratos',
        'premiooucusto_da_operacao',
        'resultado',
        'comentarios',
    ]