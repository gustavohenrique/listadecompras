# coding: utf-8
from django.test import TestCase

from model_mommy import mommy

from lista.models import *
from lista.domain import ListaDeCompras


class ListaDeComprasTest(TestCase):

    def test_obter_resumo_das_listas(self):
        guanabara = mommy.make_one(Supermercado, nome='guanabara')
        prezunic = mommy.make_one(Supermercado, nome='prezunic')
        extra = mommy.make_one(Supermercado, nome='extra')

        pepsi = mommy.make_one(Produto, nome='pepsi')
        l1 = mommy.make_one(Lista, produto=pepsi, supermercado=guanabara, preco_unitario=2, quantidade=1)
        l2 = mommy.make_one(Lista, produto=pepsi, supermercado=prezunic, preco_unitario=6, quantidade=1)
        l3 = mommy.make_one(Lista, produto=pepsi, supermercado=extra, preco_unitario=1, quantidade=2)

        biscoito = mommy.make_one(Produto, nome='biscoito')

        l4 = mommy.make_one(Lista, produto=biscoito, supermercado=guanabara, preco_unitario=2, quantidade=2)
        l5 = mommy.make_one(Lista, produto=biscoito, supermercado=prezunic, preco_unitario=1, quantidade=3)
        l6 = mommy.make_one(Lista, produto=biscoito, supermercado=extra, preco_unitario=3, quantidade=1)

        listas = [l1, l2, l3, l4, l5, l6]

        retorno_esperado = {
            'pepsi': {'guanabara': '2', 'prezunic': '6', 'extra': '2'},
            'biscoito': {'guanabara': '4', 'prezunic': '3', 'extra': '3'}
        }

        self.assertEquals(ListaDeCompras().exibir(listas), retorno_esperado)
