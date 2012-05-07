# coding: utf-8
from django.test import TestCase

from model_mommy import mommy
from lista.models import *


class SimpleTest(TestCase):
    def test_basic_addition(self):
        pepsi = mommy.make_one(Produto, nome='Pepsi')

        guanabara = mommy.make_one(Supermercado, nome='guanabara')
        preco_pepsi_guanabara = mommy.make_one(Preco, produto=pepsi, supermercado=guanabara, preco=4.5)
        #import ipdb; ipdb.set_trace()
        prezunic = mommy.make_one(Supermercado, nome='prezunic')
        preco_pepsi_prezunic = mommy.make_one(Preco, produto=pepsi, supermercado=prezunic, preco=3.5)

        extra = mommy.make_one(Supermercado, nome='extra')
        preco_pepsi_extra = mommy.make_one(Preco, produto=pepsi, supermercado=extra, preco=3)

