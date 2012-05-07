# -*- coding: utf-8 -*-
from django.contrib import admin
from lista.models import *

admin.site.register(Secao)
admin.site.register(Produto)
admin.site.register(Supermercado)

class PrecoAdmin(admin.ModelAdmin):
    list_display = ('produto', 'supermercado', 'preco', 'atualizacao')
    list_filter = ('supermercado', 'atualizacao')
admin.site.register(Preco, PrecoAdmin)
