# -*- coding: utf-8 -*-
from django.contrib import admin
from lista.models import *


class PrecoAdminInline(admin.TabularInline):
    model = Preco


class ProdutoAdmin(admin.ModelAdmin):
    inlines = [
        PrecoAdminInline,
    ]
admin.site.register(Produto, ProdutoAdmin)


class PrecoAdmin(admin.ModelAdmin):
    list_display = ('produto', 'supermercado', 'valor', 'atualizacao')
    list_filter = ('supermercado', 'atualizacao')
    ordering = ('produto', 'supermercado')
admin.site.register(Preco, PrecoAdmin)


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
