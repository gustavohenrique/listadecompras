# -*- coding: utf-8 -*-
from django.contrib import admin
from lista.models import *


class PrecificacaoAdminInline(admin.TabularInline):
    model = Precificacao


class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome')
    inlines = [
        PrecificacaoAdminInline,
    ]
admin.site.register(Produto, ProdutoAdmin)


class PrecificacaoAdmin(admin.ModelAdmin):
    list_display = ('produto', 'supermercado', 'preco', 'atualizacao')
    list_filter = ('supermercado', 'atualizacao')
    ordering = ('produto', 'supermercado')
admin.site.register(Precificacao, PrecificacaoAdmin)


class SupermercadoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'ativo')
    actions = ['ativar']

    def ativar(self, request, queryset):
        rows_updated = queryset.update(ativo=True)
        msg = '1 supermercado foi marcado como ativo' if rows_updated == 1 else '%s supermercados foram marcados como ativos' % rows_updated
        self.message_user(request, msg)

    ativar.short_description = 'Marcar como ativo'
admin.site.register(Supermercado, SupermercadoAdmin)


admin.site.register(Secao)
admin.site.register(Cotacao)
