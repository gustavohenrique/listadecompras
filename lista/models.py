# -*- coding: utf-8 -*-
from django.db import models


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


class Preco(models.Model):
    supermercado = models.ForeignKey(Supermercado)
    produto = models.ForeignKey(Produto)
    valor = models.DecimalField(max_digits=12, decimal_places=2)
    atualizacao = models.DateField(auto_now=True, auto_now_add=True)

    def __unicode__(self):
        return '%s' % self.valor

    class Meta:
        unique_together = ('supermercado', 'produto', 'valor')
        ordering = ['supermercado', '-atualizacao']


class Lista(models.Model):
    supermercado = models.ForeignKey(Supermercado)
    produto = models.ForeignKey(Produto)
    nome = models.CharField(max_length=20)
    preco_unitario = models.DecimalField(max_digits=12, decimal_places=2)
    quantidade = models.PositiveSmallIntegerField()
    criada_em = models.DateField(auto_now_add=True)

    def __unicode__(self):
        return '%s' % self.criada_em

    @property
    def preco_final(self):
        return '%s' % (self.preco_unitario * self.quantidade)
