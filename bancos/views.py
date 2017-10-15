from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, UpdateView

from braces.views import LoginRequiredMixin

from bancos.models import (
	Banco, CuentaBanco, Chequera, Cheque)
from bancos.forms import BancoForm, CuentaBancoForm
from pagos.models import Pago

class BancoCreateView(CreateView):
	model = Banco
	form_class = BancoForm
	template_name = 'bancos/banco_form.html'


class BancoDetailView(DetailView):
	model = Banco
	template_name = 'bancos/banco_detail.html'


class BancoListView(ListView):
    model = Banco
    template_name = "bancos/banco_list.html"


class CuentaBancoCreateView(CreateView):
    model = CuentaBanco
    fields = '__all__'


class CuentaBancoDetailView(DetailView):
    model = CuentaBanco
    template_name = "bancos/cuentabanco_detail.html"


class CuentaBancoListView(ListView):
    model = CuentaBanco
    template_name = "bancos/cuentabanco_list.html"


class CuentaBancoUpdateView(UpdateView):
    model = CuentaBanco
    form_class = CuentaBancoForm


class ChequeraCreateView(CreateView):
    model = Chequera
    fields = '__all__'


class ChequeraDetailView(DetailView):
    model = Chequera
