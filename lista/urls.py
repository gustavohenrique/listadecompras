from django.conf.urls import patterns, include, url


urlpatterns = patterns('',
    url(r'^$', 'lista.views.index', name='lista-index'),
    url(r'^resumo/$', 'lista.views.resumo', name='lista-resumo'),
)
