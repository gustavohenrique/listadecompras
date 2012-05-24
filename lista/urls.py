from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'^$', 'lista.views.index', name='lista-index'),
    url(r'^resumo/$', 'lista.views.resumo', name='lista-resumo'),
    url(r'^produtos/(?P<secao_id>[^/]+)', 'lista.views.produtos', name='lista-produtos-por-secao'),
    url(r'^finalizar/$', 'lista.views.finalizar', name='lista-finalizar'),
    url(r'^exibir/(?P<codigo>\w+)$', 'lista.views.exibir', name='lista-exibir'),
    url(r'^recentes/$', 'lista.views.recentes', name='lista-recentes'),
    #url(r'^produtos/(?P<secao_id>)\d/$', 'lista.views.produtos', name='lista-produtos-por-secao'),
)
