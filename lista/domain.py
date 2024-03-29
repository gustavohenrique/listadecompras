# -*- coding: utf-8 -*-


class ListaDeCompras(object):

    def exibir(self, cotacoes):
        retorno = {}
        for cotacao in cotacoes:
            nome_secao = cotacao.produto.secoes.all()[0].nome

            if not nome_secao in retorno:
                retorno.update({nome_secao: {}})

            produtos = retorno.get(nome_secao)
            nome_produto = cotacao.produto.nome
            if not nome_produto in produtos:
                produtos.update({nome_produto: {'quantidade': cotacao.quantidade, 'precos': {}}})

            precos = produtos.get(nome_produto).get('precos')
            precos.update({cotacao.supermercado.nome: cotacao.preco_final})
        return retorno

    def recentes(self, cotacoes):
        retorno = {}
        for cotacao in cotacoes:
            retorno.update({cotacao.get_absolute_url(): cotacao.atualizacao})
        return retorno
