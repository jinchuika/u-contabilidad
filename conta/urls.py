from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.views import static

urlpatterns = [
	# Administración y usuarios
    url(r'^login/$', auth_views.login, {'template_name': 'base/login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, name='logout'),
    url(r'^admin/', admin.site.urls),

    # Documentación
    url(r'^docs/$', static.serve, {'document_root': settings.DOCS_ROOT, 'path': 'search.html'}),
    url(r'^docs/(?P<path>.+)$', static.serve, {'document_root': settings.DOCS_ROOT}),

    # Aplicaciones
    url(r'^bancos/', include('bancos.urls')),
    url(r'^inventario/', include('inventario.urls')),
    url(r'^pagos/', include('pagos.urls')),
    url(r'^', include('contabilidad.urls')),
]
