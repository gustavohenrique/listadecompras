# coding: utf-8
from django.test import TestCase

from model_mommy import mommy
from lista.models import *


class SimpleTest(TestCase):
    def test_basic_addition(self):
        pepsi = Produto, nome='Pepsi')
        guanabara = mommy.make_one(Supermercado, nome='guanabara')
        precos_pepsi = mommy.make_one(Preco, produto=pepsi, supermercado=guanabara, preco=4.5)
        #import ipdb; ipdb.set_trace()
        
