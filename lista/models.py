# -*- coding: utf-8 -*-
from django.db import models

class Fabricante(models.Model):
    nome = models.CharField(unique=True, max_length=50)

    def __unicode__(self):
        return self.nome

class Secao(models.Model):
    nome = models.CharField(unique=True, max_length=50)

    class Meta:
        verbose_name_plural = u'Seções'

    def __unicode__(self):
        return self.nome

class Produto(models.Model):
    fabricante = models.ForeignKey(Fabricante, null=True, blank=True)
    secao = models.ManyToManyField(Secao)
    nome = models.CharField(unique=True, max_length=200)

    def __unicode__(self):
        return self.nome

class Supermercado(models.Model):
    nome = models.CharField(unique=True, max_length=50)

    def __unicode__(self):
        return self.nome


class Preco(models.Model):
    supermercado = models.ForeignKey(Supermercado)
    produto = models.ForeignKey(Produto)
    preco = models.DecimalField(max_digits=12, decimal_places=2)
    atualizacao = models.DateField(auto_now=True, auto_now_add=True)

    def __unicode__(self):
        return self.preco
