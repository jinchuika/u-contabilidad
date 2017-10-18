from django.views.generic import DetailView, ListView, TemplateView
from django.views.generic.edit import CreateView, UpdateView

from braces.views import LoginRequiredMixin

from pagos.models import FacturaCompra
from contabilidad.models import CuentaContable


class HomeView(LoginRequiredMixin, TemplateView):
    template_name = "base/base.html"


class CuentaContableCreateView(LoginRequiredMixin, CreateView):
    model = CuentaContable
    fields = '__all__'


class CuentaContableListView(LoginRequiredMixin, ListView):
    model = CuentaContable


class CuentaContableDetailView(LoginRequiredMixin, DetailView):
    model = CuentaContable


class FacturaPendienteListView(ListView):
    queryset = FacturaCompra.pendientes.all()
    template_name = "contabilidad/cuentas_pendientes.html"
    context_object_name = 'pendientes_list'

    def get_context_data(self, **kwargs):
        context = super(FacturaPendienteListView, self).get_context_data(**kwargs)
        print(context)
        return context
