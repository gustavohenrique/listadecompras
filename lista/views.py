# -*- coding: utf-8 -*-
from django.views.generic.simple import direct_to_template
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.core.urlresolvers import reverse
from django.core import serializers
from django.utils import simplejson
from django.conf import settings

from lista.models import Secao, Produto, Lista
from lista.domain import ListaDeCompras


def index(request):
    context = {'secoes': Secao.objects.all()}
    return direct_to_template(request, 'index.html', context)


def produtos(request, secao_id):
    secao = get_object_or_404(Secao, pk=secao_id)
    context = {'produtos': secao.produto_set.all(), 'secao': secao}
    return direct_to_template(request, 'produtos.html', context)


def resumo(request):
    if request.POST:
        lista_ids = request.POST.get('ids').split(',')
        lista = []
        for id in lista_ids:
            try:
                pk = int(id)
                produto = Produto.objects.get(pk=pk)
                lista.append(produto)
            except:
                pass

        return direct_to_template(request, 'resumo.html', {'lista': lista})
    return HttpResponseRedirect(reverse('lista-index'))


def finalizar(request):
    if request.is_ajax() and request.method == 'POST':
        produtos = request.POST.keys()
        codigo = ListaDeCompras().pega_identificador_unico()
        for produto_id in produtos:
            try:
                quantidade = request.POST.get(produto_id)
                if int(quantidade) > 0:
                    produto = Produto.objects.get(pk=produto_id)

                    lista = Lista()
                    lista.produto = produto
                    lista.quantidade = quantidade
                    lista.codigo = codigo
                    lista.save()
            except:
                pass

        url = '/'.join([settings.LISTA_BASE_URL, codigo])
        json = simplejson.dumps({'url': url})
        return HttpResponse(json, mimetype='application/json')

    raise Http404


def exibir(request, codigo):
    listas = Lista.objects.filter(codigo=codigo)
    lista_de_compras = ListaDeCompras().exibir(listas)

    context = {'lista_de_compras': lista_de_compras}
    return direct_to_template(request, 'lista.html', context)


# def produtos(request, secao_id):
#     secao = get_object_or_404(Secao, pk=secao_id)
#     produtos = secao.produto_set.all()

#     if produtos.count() > 0:
#         json = serializers.serialize('json', produtos, fields=('id', 'nome'))
#         return HttpResponse(json, mimetype='application/json')
#     else:
#         raise Http404


def recentes(request):
    listas = Lista.objects.all()
    context = {'recentes': ListaDeCompras().recentes(listas)}
    return direct_to_template(request, 'recentes.html', context)



