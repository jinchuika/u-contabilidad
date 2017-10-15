from django.conf.urls import url

from contabilidad import views as contabilidad_views

urlpatterns = [
    url(r'^cuentacontable/add/$', contabilidad_views.CuentaContableCreateView.as_view(), name='cuentacontable_add'),
    url(r'^cuentacontable/list/$', contabilidad_views.CuentaContableListView.as_view(), name='cuentacontable_list'),
    url(r'^cuentacontable/(?P<pk>\d+)/$', contabilidad_views.CuentaContableDetailView.as_view(), name='cuentacontable_detail'),
    url(r'^$', contabilidad_views.HomeView.as_view(), name='home'),
]
