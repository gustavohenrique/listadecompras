from django.conf.urls import patterns, include, url


urlpatterns = patterns('',
    url(r'^$', 'lista.views.index', name='lista-index'),
    url(r'^resumo/$', 'lista.views.resumo', name='lista-resumo'),
    url(r'^produtos/(?P<secao_id>[^/]+)', 'lista.views.produtos', name='lista-produtos-por-secao'),
    #url(r'^produtos/(?P<secao_id>)\d/$', 'lista.views.produtos', name='lista-produtos-por-secao'),
)
