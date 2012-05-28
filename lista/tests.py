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

        pepsi = mommy.make_one(Produto, nome='pepsi', secoes=[bebidas])
        l1 = mommy.make_one(Lista, codigo='abcd', produto=pepsi)
        l2 = mommy.make_one(Lista, codigo='abcd', produto=pepsi)
        l3 = mommy.make_one(Lista, codigo='abcd', produto=pepsi)

        guarana = mommy.make_one(Produto, nome='guarana', secoes=[bebidas])

        l4 = mommy.make_one(Lista, codigo='efgh', produto=guarana)
        l5 = mommy.make_one(Lista, codigo='efgh', produto=guarana)
        l6 = mommy.make_one(Lista, codigo='efgh', produto=guarana)

        passatempo = mommy.make_one(Produto, nome='passatempo', secoes=[biscoitos])

        l7 = mommy.make_one(Lista, codigo='ijkl', produto=passatempo)
        l8 = mommy.make_one(Lista, codigo='ijkl', produto=passatempo)
        l9 = mommy.make_one(Lista, codigo='ijkl', produto=passatempo)

        listas = [l1, l2, l3, l4, l5, l6, l7, l8, l9]

        retorno_esperado = {
            u'bebidas': {
                'pepsi': {'id': 1},
                'guarana': {'id': 2}
            },
            u'biscoitos e bomboniere': {
                'passatempo': {'id': 3}
            }
        }

        self.assertEquals(ListaDeCompras().exibir(listas), retorno_esperado)
