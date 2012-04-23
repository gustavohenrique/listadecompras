# -*- coding: utf-8 -*-
from django.views.generic.simple import direct_to_template
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect, HttpResponsePermanentRedirect
from django.core.urlresolvers import reverse

def index(request):
    return direct_to_template(request, 'index.html')

def resumo(request):
    return direct_to_template(request, 'resumo.html')