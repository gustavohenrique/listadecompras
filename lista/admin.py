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


admin.site.register(Secao)
admin.site.register(Supermercado)
