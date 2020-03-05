# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Operacoes(models.Model):
    class Meta:
        verbose_name_plural = 'Operações'

    #DATA DE ABERTURA DA OPERAÇÃO:

    data_abertura = models.DateField(
        'Data de abertura:',
        blank=True,
        null=True
    )

    #DATA DE FECHAMENTO DA OPERAÇÃO:

    data_fechamento = models.DateField(
        'Data de fechamento:',
        blank=True,
        null=True
    )

    #DATA DE VENCIMENTO DAS OPÇÕES:

    vencimento_das_opcoes = models.DateField(
        'Data de vencimento das opções:',
        blank=True,
        null=True
    )

    nivel_vol_implicita = models.DecimalField(
        'Nível de Vol. Implicita na data:',
        max_digits=50,
        decimal_places=1,
        blank=True,
        null=True
    )

    #SERIE DE VENCIMENTO CALL/PUT:

    serie_vencimento_choices = (
        ('Janeiro - A/M', 'Janeiro - A/M'),
        ('Fevereiro - B/N', 'Fevereiro B/N'),
        ('Março - C/O', 'Março - C/O'),
        ('Abril - D/P', 'Abril - D/P'),
        ('Maio - E/Q', 'Maio - E/Q'),
        ('Junho - F/R', 'Junho - F/R'),
        ('Julho - G/S', 'Julho - G/S'),
        ('Agosto - H/T', 'Agosto H/T'),
        ('Setembro - I/U', 'Setembro I/U'),
        ('Outubro - J/V', 'Outubro - J/V'),
        ('Novembro - K/W', 'Novembro - K/W'),
        ('Dezembro - L/X', 'Dezembro - L/X')
    )

    serie_vencimento_opcoes = models.CharField(
        'Serie de vencimento das opções:',
        max_length=50,
        blank=True,
        choices=serie_vencimento_choices
    )

    #TICKER DO ATIVO SUBJACENTE:

    ticker_ativo_subjacente = models.CharField(
        'Ticker do ativo subjacente:',
        max_length=30,
        blank=True,
        default='PETR4'
    )

    
    motivo_da_operacao = models.CharField(
        'Motivo da operação:',
        max_length=50,
        blank=True
    )

    #TIMEFRAME DO GRÁFICO UTILIZAOD:

    timeframe_do_grafico_choices = (
        ('Diário', 'Diário'),
        ('Semanal', 'Semanal'),
        ('Mensal', 'Mensal')
    )
    timeframe_do_grafico = models.CharField(
        'TimeFrame do gráfico utililizado:',
        blank=True,
        max_length=30,
        default='Diário',
        choices=timeframe_do_grafico_choices
    )

    #SELEÇÃO DE ESTRATÉGIAS DE ALTA:
    
    estrategia_de_alta_choices = (
        ('Long Call', 'Long Call'),
        ('Bull Call Spread', 'Bull Call Spread'),
        ('Short Put', 'Short Put'),
        ('Long Put Spread', 'Long Put Spread'),
        ('Covered Call', 'Covered Call'),
        ('Covered Strangle', 'Covered Strangle'),
        ('Married (Protective) Put', 'Married (Protective) Put'),
        ('The Collar', 'The Collar'),
        ('Synthetic Long Stock', 'Synthetic Long Stock')
    )
    estrategia_de_alta = models.CharField(
        'Estratégia de alta utilizada:',
        max_length=50,
        blank=True,
        choices=estrategia_de_alta_choices
    )

    #ESTRATÉGIAS DE BAIXA:

    estrategia_de_baixa_choices = (
        ('Long Put', 'Long Put'),
        ('Short Put Spread', 'Short Put Spread'),
        ('Short Call', 'Short Call'),
        ('Short Iron Butterflies', 'Short Iron Butterflies'),
        ('Covered Put', 'Covered Put'),
        ('Synthetic Long Stock', 'Synthetic Long Stock')
    )
    estrategia_de_baixa = models.CharField(
        'Estratégia de baixa utilizada:',
        max_length=50,
        blank=True,
        choices=estrategia_de_baixa_choices
    )

    #ESTRATÉGIAS DE LATERALIDADE:

    estrategia_de_lateralidade_choices = (
        ('Short Strangle', 'Short Strangle'),
        ('Short Straddle', 'Short Straddle'),
        ('Short Iron Condor', 'Short Iron Condor'),
        ('Short Iron Butterfly', 'Short Iron Butterfly'),
        ('Long Butterfly', 'Long Butterfly'),
        ('Long Condor', 'Long Condor'),
        ('Short Condor', 'Short Condor'),
        ('Long Strangle', 'Long Strangle'),
        ('Long Straddle', 'Long Straddle'),
        ('Long Iron Condor', 'Long Iron Condor'),
        ('Long Iron Butterfly', 'Long Iron Butterfly')
    )
    estrategia_de_lateralidade = models.CharField(
        'Estratégia de lateralidade utilizada:',
        max_length=50,
        blank=True,
        choices=estrategia_de_lateralidade_choices
    )

    contratos = models.IntegerField(
        'N. de contratos:',
        blank=True,
        null=True
    )

    premiooucusto_da_operacao = models.DecimalField(
        'Premio/Custo da operação',
        max_digits=50,
        decimal_places=2,
        blank=True,
        null=True
    )

    resultado = models.DecimalField(
        'Resultado da Op.:',
        max_digits=50,
        decimal_places=2,
        blank=True,
        null=True
    )

    comentarios = models.TextField(
        'Comentários:',
        blank=True,
    )
