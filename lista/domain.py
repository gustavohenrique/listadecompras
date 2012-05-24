# -*- coding: utf-8 -*-
from datetime import datetime
from django.utils.http import int_to_base36


class ListaDeCompras(object):

    def exibir(self, listas):
        retorno = {}
        for lista in listas:
            nome_secao = lista.produto.secoes.all()[0].nome

            if not nome_secao in retorno:
                retorno.update({nome_secao: {}})

            produtos = retorno.get(nome_secao)
            nome_produto = lista.produto.nome
            if not nome_produto in produtos:
                produtos.update({nome_produto: {'id': lista.produto.id, 'quantidade': lista.quantidade}})

        return retorno

    def recentes(self, listas):
        retorno = {}
        for lista in listas:
            retorno.update({lista.get_absolute_url(): lista.atualizacao})
        return retorno

    def pega_identificador_unico(self):
        miliseconds = datetime.now().microsecond
        return int_to_base36(miliseconds)
