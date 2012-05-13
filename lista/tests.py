# coding: utf-8
from django.test import TestCase

from model_mommy import mommy

from lista.models import *
from lista.domain import ListaDeCompras


class ListaDeComprasTest(TestCase):

    def test_obter_lista_de_compras_com_preco_x_quantidade_por_produto(self):
        self.maxDiff = None
        bebidas = mommy.make_one(Secao, nome='bebidas')
        biscoitos = mommy.make_one(Secao, nome='biscoitos e bomboniere')

        guanabara = mommy.make_one(Supermercado, nome='guanabara')
        prezunic = mommy.make_one(Supermercado, nome='prezunic')
        extra = mommy.make_one(Supermercado, nome='extra')

        pepsi = mommy.make_one(Produto, nome='pepsi', secoes=[bebidas])
        l1 = mommy.make_one(Cotacao, codigo='abcd', produto=pepsi, supermercado=guanabara, preco=2, quantidade=2)
        l2 = mommy.make_one(Cotacao, codigo='abcd', produto=pepsi, supermercado=prezunic, preco=6, quantidade=2)
        l3 = mommy.make_one(Cotacao, codigo='abcd', produto=pepsi, supermercado=extra, preco=1, quantidade=2)

        guarana = mommy.make_one(Produto, nome='guarana', secoes=[bebidas])

        l4 = mommy.make_one(Cotacao, codigo='efgh', produto=guarana, supermercado=guanabara, preco=2, quantidade=3)
        l5 = mommy.make_one(Cotacao, codigo='efgh', produto=guarana, supermercado=prezunic, preco=1, quantidade=3)
        l6 = mommy.make_one(Cotacao, codigo='efgh', produto=guarana, supermercado=extra, preco=3, quantidade=3)

        passatempo = mommy.make_one(Produto, nome='passatempo', secoes=[biscoitos])

        l7 = mommy.make_one(Cotacao, codigo='ijkl', produto=passatempo, supermercado=guanabara, preco=2, quantidade=1)
        l8 = mommy.make_one(Cotacao, codigo='ijkl', produto=passatempo, supermercado=prezunic, preco=0, quantidade=1)
        l9 = mommy.make_one(Cotacao, codigo='ijkl', produto=passatempo, supermercado=extra, preco=3, quantidade=1)

        cotacoes = [l1, l2, l3, l4, l5, l6, l7, l8, l9]

        retorno_esperado = {
            u'bebidas': [{
                'produto': 'pepsi', 'quantidade': '2', 'precos': {'guanabara': '4', 'prezunic': '12', 'extra': '2'}},
                {'produto': 'guarana', 'quantidade': '3', 'precos': {'guanabara': '4', 'prezunic': '3', 'extra': '3'}}
            ],
            u'biscoitos e bomboniere': [{
                'produto': 'passatempo', 'quantidade': '1', 'precos': {'guanabara': '2', 'prezunic': '0', 'extra': '3'}
            }]
        }

        self.assertEquals(ListaDeCompras().exibir(cotacoes), retorno_esperado)
