# -*- coding: utf-8 -*-
from django.contrib import admin
from lista.models import *


class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'minhas_secoes')
    list_display_links = ('nome',)
    search_fields = ['nome']
    filter_horizontal = ('secoes',)

    def minhas_secoes(self, obj):
        secoes = ''
        for s in obj.secoes.all():
            secoes += '%s, ' % s.nome
        return secoes[0: len(secoes) - 2]
    minhas_secoes.short_description = u'Seções'

admin.site.register(Produto, ProdutoAdmin)

admin.site.register(Secao)
