from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.views import static

urlpatterns = [
    url(r'^docs/$', static.serve, {'document_root': settings.DOCS_ROOT, 'path': 'search.html'}),
    url(r'^docs/(?P<path>.+)$', static.serve, {'document_root': settings.DOCS_ROOT}),
    url(r'^bancos/', include('bancos.urls')),
    url(r'^inventario/', include('inventario.urls')),
    url(r'^contabilidad/', include('contabilidad.urls')),
    url(r'^pagos/', include('pagos.urls')),
    url(r'^admin/', admin.site.urls),
]
