# -*- coding: utf-8 -*-


class ListaDeCompras(object):

    def exibir(self, listas):
        retorno = {}
        for lista in listas:
            key = lista.produto.nome

            if not key in retorno:
                retorno.update({key: {}})
            d = retorno.get(key)
            d.update({lista.supermercado.nome: lista.preco_final})
        return retorno
