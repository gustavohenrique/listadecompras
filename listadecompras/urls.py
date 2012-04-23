from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'lista.views.index', name='index'),
    url(r'^lista/', include('lista.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)

from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns += staticfiles_urlpatterns()

# from django.conf import settings
# from django.views.generic.simple import direct_to_template
# if settings.DEBUG:
#     urlpatterns += patterns('',
#          (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT, 'show_indexes': True}),
#          ('^404/$', direct_to_template, {'template': '404.html'}),
#          ('^500/$', direct_to_template, {'template': '500.html'})
#     )