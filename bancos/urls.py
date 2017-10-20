from django.conf.urls import url

from bancos import views as bancos_views

urlpatterns = [
    url(r'^banco/add/$', bancos_views.BancoCreateView.as_view(), name='banco_add'),
    url(r'^banco/(?P<pk>\d+)/$', bancos_views.BancoDetailView.as_view(), name='banco_detail'),
    url(r'^banco/list/$', bancos_views.BancoListView.as_view(), name='banco_list'),

    url(r'^cuenta/add/$', bancos_views.CuentaBancoCreateView.as_view(), name='cuenta_add'),
    url(r'^cuenta/(?P<pk>\d+)/$', bancos_views.CuentaBancoDetailView.as_view(), name='cuenta_detail'),
    url(r'^cuenta/(?P<pk>\d+)/update/$', bancos_views.CuentaBancoUpdateView.as_view(), name='cuenta_update'),
    url(r'^cuenta/list/$', bancos_views.CuentaBancoListView.as_view(), name='cuenta_list'),

    url(r'^chequera/add/$', bancos_views.ChequeraCreateView.as_view(), name='chequera_add'),
    url(r'^chequera/(?P<pk>\d+)/$', bancos_views.ChequeraDetailView.as_view(), name='chequera_detail'),

    url(r'^deposito/add/$', bancos_views.DepositoBancoCreateView.as_view(), name='deposito_add'),
    url(r'^deposito/(?P<pk>\d+)/$', bancos_views.DepositoBancoDetailView.as_view(), name='deposito_detail'),
    url(r'^deposito/(?P<pk>\d+)/print/$', bancos_views.DepositoBancoPrintView.as_view(), name='deposito_print'),

    url(r'^cheque/(?P<pk>\d+)/print/$', bancos_views.ChequePrintView.as_view(), name='cheque_print'),
]
