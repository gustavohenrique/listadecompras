# -*- coding: utf-8 -*-
from django.views.generic.simple import direct_to_template
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect, HttpResponsePermanentRedirect, HttpResponse, Http404
from django.core.urlresolvers import reverse
from django.core import serializers


from lista.models import Secao, Produto

def index(request):
    context = {'secoes': Secao.objects.all()}
    return direct_to_template(request, 'index.html', context)

def resumo(request):
    return direct_to_template(request, 'resumo.html')

def produtos(request, secao_id):
    secao = get_object_or_404(Secao, pk=secao_id)
    produtos = Produto.objects.filter(secao=secao)
    if produtos.count() > 0:
        json = serializers.serialize('json', produtos, fields=('id','nome'))
        return HttpResponse(json, mimetype='application/json')
    else:
        raise Http404
