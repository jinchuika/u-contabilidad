from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^bancos/', include('bancos.urls')),
    url(r'^inventario/', include('inventario.urls')),
    url(r'^contabilidad/', include('contabilidad.urls')),
    url(r'^pagos/', include('pagos.urls')),
    url(r'^admin/', admin.site.urls),
]
