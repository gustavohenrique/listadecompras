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


class Lista(models.Model):
    produto = models.ForeignKey(Produto)
    codigo = models.CharField(max_length=20)
    quantidade = models.PositiveSmallIntegerField()
    atualizacao = models.DateField(auto_now=True, auto_now_add=True)

    def __unicode__(self):
        return '%s' % self.codigo

    class Meta:
        ordering = ['atualizacao', 'produto']

    def get_absolute_url(self):
        return '%s/%s' % (settings.LISTA_BASE_URL, self.codigo)
