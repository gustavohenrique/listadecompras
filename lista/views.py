# -*- coding: utf-8 -*-
from django.views.generic.simple import direct_to_template
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.core.urlresolvers import reverse
from django.core import serializers

from lista.models import Secao, Produto, Supermercado, Precificacao, Cotacao
from lista.domain import ListaDeCompras


def index(request):
    context = {'secoes': Secao.objects.all()}
    return direct_to_template(request, 'index.html', context)


def resumo(request):
    if request.POST:
        lista_ids = request.POST.get('ids').split(',')
        precos = []
        for id in lista_ids:
            try:
                pk = int(id)
                produto = Produto.objects.get(pk=pk)
                precos.append(Precificacao.objects.filter(produto=produto))
            except:
                pass

        context = {'lista': precos, 'supermercados': Supermercado.objects.filter(ativo=True)}
        return direct_to_template(request, 'resumo.html', context)
    return HttpResponseRedirect(reverse('lista-index'))


def salvar(request):
    if request.is_ajax() and request.method == 'POST':
        produtos = request.POST.keys()
        codigo = _pega_identificador_unico()
        for produto_id in produtos:
            try:
                quantidade = request.POST.get(produto_id)
                if int(quantidade) > 0:
                    produto = Produto.objects.get(pk=produto_id)
                    precificacoes = Precificacao.objects.filter(produto=produto)

                    for precificacao in precificacoes:
                        cotacao = Cotacao()
                        cotacao.supermercado = precificacao.supermercado
                        cotacao.produto = precificacao.produto
                        cotacao.codigo = codigo
                        cotacao.quantidade = quantidade
                        cotacao.preco = precificacao.preco
                        cotacao.save()
            except:
                pass

        from django.utils import simplejson
        from django.conf import settings

        url = '/'.join([settings.LISTA_BASE_URL, codigo])
        json = simplejson.dumps({'url': url})
        return HttpResponse(json, mimetype='application/json')

    raise Http404


def exibir(request, codigo):
    cotacoes = Cotacao.objects.filter(codigo=codigo)
    lista_de_compras = ListaDeCompras().exibir(cotacoes)

    context = {'lista_de_compras': lista_de_compras, 'supermercados': Supermercado.objects.filter(ativo=True)}
    return direct_to_template(request, 'lista.html', context)


def produtos(request, secao_id):
    secao = get_object_or_404(Secao, pk=secao_id)
    produtos = secao.produto_set.all()

    if produtos.count() > 0:
        json = serializers.serialize('json', produtos, fields=('id', 'nome'))
        return HttpResponse(json, mimetype='application/json')
    else:
        raise Http404


def _pega_identificador_unico():
    from datetime import datetime
    from django.utils.http import int_to_base36
    miliseconds = datetime.now().microsecond
    return int_to_base36(miliseconds)
