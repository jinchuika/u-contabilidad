from django.conf.urls import url

from pagos import views as pagos_views

urlpatterns = [
    url(r'^proveedor/add/$', pagos_views.ProveedorCreateView.as_view(), name='proveedor_add'),
    url(r'^proveedor/list/$', pagos_views.ProveedorListView.as_view(), name='proveedor_list'),
    url(r'^proveedor/(?P<pk>\d+)/$', pagos_views.ProveedorDetailView.as_view(), name='proveedor_detail'),

    url(r'^factura/add/$', pagos_views.FacturaCompraCreateView.as_view(), name='factura_add'),
    url(r'^factura/(?P<pk>\d+)/$', pagos_views.FacturaCompraDetailView.as_view(), name='factura_detail'),
    url(r'^factura/(?P<pk>\d+)/update/$', pagos_views.FacturaCompraUpdateView.as_view(), name='factura_update'),

    url(r'^facturadetalle/add/$', pagos_views.FacturaCompraDetalleCreateView.as_view(), name='facturadetalle_add'),
]
