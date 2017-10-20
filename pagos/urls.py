from django.conf.urls import url
from django.views.decorators.cache import cache_page

from pagos import views as pagos_views
from pagos import api_views


factura_api_list = api_views.FacturaCompraViewSet.as_view({
    'get': 'list'})

urlpatterns = [
    url(r'^proveedor/add/$', pagos_views.ProveedorCreateView.as_view(), name='proveedor_add'),
    url(r'^proveedor/list/$', pagos_views.ProveedorListView.as_view(), name='proveedor_list'),
    url(r'^proveedor/(?P<pk>\d+)/$', pagos_views.ProveedorDetailView.as_view(), name='proveedor_detail'),

    url(r'^factura/add/$', pagos_views.FacturaCompraCreateView.as_view(), name='factura_add'),
    url(r'^factura/list/$', pagos_views.FacturaCompraListView.as_view(), name='factura_list'),
    url(r'^factura/(?P<pk>\d+)/$', cache_page(1)(pagos_views.FacturaCompraDetailView.as_view()), name='factura_detail'),
    url(r'^factura/(?P<pk>\d+)/update/$', pagos_views.FacturaCompraUpdateView.as_view(), name='factura_update'),

    url(r'^factura/(?P<pk>\d+)/pagar/$', pagos_views.PagoCreateView.as_view(), name='factura_pagar'),

    url(r'^facturadetalle/add/$', pagos_views.FacturaCompraDetalleCreateView.as_view(), name='facturadetalle_add'),

    url(r'^pago/add/$', pagos_views.PagoCreateView.as_view(), name='pago_add'),

    url(r'^api/factura/$', factura_api_list, name='factura_api_list'),
]
