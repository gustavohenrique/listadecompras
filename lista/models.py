# -*- coding: utf-8 -*-
from django.db import models
from django.conf import settings


class Secao(models.Model):
    nome = models.CharField(unique=True, max_length=50)

    class Meta:
        verbose_name_plural = u'Seções'

    def __unicode__(self):
        return self.nome


class Produto(models.Model):
    secoes = models.ManyToManyField(Secao)
    nome = models.CharField(unique=True, max_length=200)

    def __unicode__(self):
        return self.nome


class Supermercado(models.Model):
    nome = models.CharField(unique=True, max_length=50)
    ativo = models.BooleanField(default=True)

    def __unicode__(self):
        return self.nome

    class Meta:
        ordering = ['nome']


class Precificacao(models.Model):
    supermercado = models.ForeignKey(Supermercado)
    produto = models.ForeignKey(Produto)
    preco = models.DecimalField(max_digits=12, decimal_places=2)
    atualizacao = models.DateField(auto_now=True, auto_now_add=True)

    def __unicode__(self):
        return '%s' % self.preco

    class Meta:
        unique_together = ('supermercado', 'produto', 'preco')
        ordering = ['supermercado', '-atualizacao']
        verbose_name_plural = u'Precificações'


class Cotacao(models.Model):
    supermercado = models.ForeignKey(Supermercado)
    produto = models.ForeignKey(Produto)
    codigo = models.CharField(max_length=20)
    quantidade = models.PositiveSmallIntegerField()
    preco = models.DecimalField(max_digits=12, decimal_places=2)
    atualizacao = models.DateField(auto_now=True, auto_now_add=True)

    def __unicode__(self):
        return '%s' % self.codigo

    class Meta:
        ordering = ['atualizacao', 'produto']

    def get_absolute_url(self):
        return '%s/%s' % (settings.LISTA_BASE_URL, self.codigo)

    @property
    def preco_final(self):
        return '%s' % (self.preco * self.quantidade)
