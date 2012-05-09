# -*- coding: utf-8 -*-
from django.views.generic.simple import direct_to_template
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.core.urlresolvers import reverse
from django.core import serializers

from lista.models import Secao, Produto, Preco, Supermercado, Lista


def index(request):
    context = {'secoes': Secao.objects.all()}
    return direct_to_template(request, 'index.html', context)


def resumo(request):
    if request.POST:
        lista_ids = request.POST.get('ids').split(',')
        produtos = []
        for id in lista_ids:
            try:
                pk = int(id)
                p = Produto.objects.get(pk=pk)
                produtos.append(Preco.objects.filter(produto=p))
            except:
                pass

        context = {'lista': produtos, 'supermercados': Supermercado.objects.filter(ativo=True)}
        return direct_to_template(request, 'resumo.html', context)
    return HttpResponseRedirect(reverse('lista-index'))


def salvar(request):
    if request.is_ajax() and request.method == 'POST':
        precos = request.POST.keys()
        lista_nome = _pega_identificador_unico()
        for preco_id in precos:
            try:
                quantidade = request.POST.get(preco_id)
                preco = Preco.objects.get(pk=preco_id)

                lista = Lista()
                lista.supermercado = preco.supermercado
                lista.produto = preco.produto
                lista.preco_unitario = preco.valor
                lista.quantidade = quantidade
                lista.nome = lista_nome
                lista.save()
            except:
                pass

        from django.utils import simplejson
        from django.conf import settings

        url = '/'.join([settings.LISTA_BASE_URL, lista_nome])
        json = simplejson.dumps({'url': url})
        return HttpResponse(json, mimetype='application/json')

    raise Http404


def exibir(request, lista_nome):
    listas = Lista.objects.filter(nome=lista_nome)
    return HttpResponse(listas)


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
