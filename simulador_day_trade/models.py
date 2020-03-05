# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Operacoes(models.Model):

    class Meta:
        verbose_name_plural = 'Operações'

    #DATA DO TRADE:

    data = models.DateField(
        'Data*:',
        blank=False
        )

    #CORRETORA

    corretora_opcoes = (
        ('CLEAR', 'CLEAR'),
        ('MODAL', 'MODAL'),
        ('XP', 'XP'),
    )
    corretora = models.CharField(
        'Corretora',
        max_length=30,
        default='CLEAR',
        blank=False,
        choices=corretora_opcoes
    )

    #HORÁRIO DE ABERTURA:

    horario_de_abertura = models.TimeField(
        'Hora de abertura da operação*:',
        blank=False
        )

    #HORÁRIO DE FECHAMENTO:

    horario_de_fechamento = models.TimeField(
        'Hora de fechamento da operação*:',
        blank=False
        )

    #CATEGORIA DE MERCADO:

    categoria_opcoes = (
        ('FUTUROS', 'FUTUROS'),
        ('OPCOES', 'OPÇÕES'),
        ('ACOES', 'AÇÕES'),
        ('FOREX', 'FOREX')
    )
    categoria = models.CharField(
        max_length=15,
        choices=categoria_opcoes,
        blank=False,
        default='FUTUROS'     
        )

    #ATIVO OPERADO:

    ativo = models.CharField(
        'Ativo*:', 
        max_length=30,
        default='WINFUT',
        blank=False
        )

    #QUANTIDADE DE CONTRATOS OU AÇÕES:

    sizing = models.IntegerField(
        'Position size*:',
        default='1',
        blank=False
    )

    #DIREÇÃO DO TRADE:

    direcao_choices = (
        ('C', 'Compra'),
        ('V', 'Venda'),
    )
    direcao = models.CharField(
        'Direção*:', 
        max_length=30, 
        choices=direcao_choices,
        blank=False
    )

    #CUSTO DE CORRETAGEM:

    corretagem = models.DecimalField(
        'Corretagem*:',
        max_digits=15,
        decimal_places=2,
        default='0',
        blank=True
    )

    #CUSTOS B3

    custos_b3 = models.DecimalField(
        'Custos B3*:',
        max_digits=15,
        decimal_places=2,
        default='0',
        blank=True
    )

    #CONTEXTO DE PREÇO:

    contexto_opcoes = (
        ('Momentum', 'Momentum'),
        ('Tendência', 'Tendência'),
        ('Consolidação', 'Conslidação')
    )

    contexto = models.CharField(
        'Contexto:',
        max_length=100,
        default='Momentum',
        blank=True,
        choices=contexto_opcoes
    )

    #SETUP DE ENTRADA:

    estrategia_opcoes = (
        ('TLP/TAB','TLP/TAB'),
        ('H/L2', 'H/L2'),
        ('H/L3', 'H/L3')
    )

    estrategia = models.CharField(
        'Estratégia*:',
        max_length=30,
        blank=False,
        default='H/L2',
        choices=estrategia_opcoes
    )

    #DISTANCIA DA MÉDIA:

    distancia_media_opcoes = (
        ('Testando MM21', 'Testando MM21'),
        ('Entre a MM21 e BK', 'Entre a MM21 e BK'),
        ('Longe da MM21', 'Longe da MM21'),
        ('Testando BK', 'Testando BK'),
        ('Acima/Abaixo da MM21', 'Acima/Abaixo da MM21')
    )

    distancia_media = models.CharField(
        'Distancia da média:',
        max_length=100,
        blank=True,
        default='Testando MM21',
        choices=distancia_media_opcoes
    )

    #TEMPO GRÁFICO DA ENTRADA:

    tempo_grafico_entrada = models.CharField(
        'Tempo gráfico da entrada*:',
        max_length=20,
        default='1 minuto',
        blank=False
    )

    #TEMPO GRÁFICO CORRELACIONADO:

    tempo_grafico_correlacionado = models.CharField(
        'Tempo gráfico correlacionado:',
        max_length=20,
        blank=True
    )

    #RISCO INICIAL:

    risco_incial = models.DecimalField(
        'Risco da Operação*:',
        max_digits=15,
        decimal_places=2,
        default='-80',
        blank=False
        )

    #RESULTADO DO TRADE:

    resultado_operacional = models.DecimalField(
        'Resultado*:',
        max_digits=15,
        decimal_places=2,
        default='-80',
        blank=False
    )

    #COMENTÁROS:

    comentarios_adicionais = models.CharField(
        'Comentários adicionais:', 
        max_length=500,
        blank=True
        )

class SimuladorDeStops(models.Model):

    class Meta:
        verbose_name_plural = 'Simulador de Stops'

    #SIMULAÇÃO DE STOPS PARA TESTE DE STRESS:

    stop_primeiro_teste = models.DecimalField(
        'Simulação Stop Nivel 1:',
        max_digits=15,
        decimal_places=2,
        blank=True,
        default='-30'
    )
    
    stop_segundo_teste = models.DecimalField(
        'Simulação Stop Nivel 2:',
        max_digits=15,
        decimal_places=2,
        blank=True,
        default='-40'
    )
    stop_terceiro_teste = models.DecimalField(
        'Simulação Stop Nivel 3:',
        max_digits=15,
        decimal_places=2,
        blank=True,
        default='-50'
    )
    stop_quarto_teste = models.DecimalField(
        'Simulação Stop Nivel 4:',
        max_digits=15,
        decimal_places=2,
        blank=True,
        default='-60'
    )
    stop_quinto_teste = models.DecimalField(
        'Simulação Stop Nivel 5:',
        max_digits=15,
        decimal_places=2,
        blank=True,
        default='-70'
    )