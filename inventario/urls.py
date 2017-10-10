from django.conf.urls import url

from inventario import views as inventario_views

urlpatterns = [
    url(r'^producto/add/$', inventario_views.ProductoCreateView.as_view(), name='producto_add'),
    url(r'^producto/list/$', inventario_views.ProductoListView.as_view(), name='producto_list'),
    url(r'^producto/(?P<pk>\d+)/$', inventario_views.ProductoDetailView.as_view(), name='producto_detail'),

    url(r'^activofijo/list/$', inventario_views.ActivoFijoListView.as_view(), name='activofijo_list'),
]
