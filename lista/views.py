# -*- coding: utf-8 -*-
from django.views.generic.simple import direct_to_template
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.core.urlresolvers import reverse
from django.core import serializers

from lista.models import Secao, Produto, Preco, Supermercado


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


def produtos(request, secao_id):
    secao = get_object_or_404(Secao, pk=secao_id)
    produtos = secao.produto_set.all()

    if produtos.count() > 0:
        json = serializers.serialize('json', produtos, fields=('id','nome'))
        return HttpResponse(json, mimetype='application/json')
    else:
        raise Http404
