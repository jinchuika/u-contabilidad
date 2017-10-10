from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, UpdateView

from pagos.models import Proveedor, FacturaCompra, FacturaCompraDetalle
from pagos.forms import (
    FacturaCompraForm, FacturaCompraCompletaForm,
    FacturaCompraDetalleForm)


class ProveedorCreateView(CreateView):
    model = Proveedor
    fields = '__all__'


class ProveedorListView(ListView):
    model = Proveedor


class ProveedorDetailView(DetailView):
    model = Proveedor


class FacturaCompraCreateView(CreateView):
    model = FacturaCompra
    form_class = FacturaCompraForm


class FacturaCompraDetailView(DetailView):
    model = FacturaCompra
    template_name = 'pagos/facturacompra_update.html'

    def get_context_data(self, **kwargs):
        context = super(FacturaCompraDetailView, self).get_context_data(**kwargs)
        context['completa_form'] = FacturaCompraCompletaForm(
            instance=self.object,
            initial={'completa': True})
        context['detalle_form'] = FacturaCompraDetalleForm(initial={
            'factura': self.object})
        return context


class FacturaCompraUpdateView(UpdateView):
    model = FacturaCompra
    form_class = FacturaCompraCompletaForm
    template_name = 'pagos/facturacompra_update.html'


class FacturaCompraDetalleCreateView(CreateView):
    model = FacturaCompraDetalle
    form_class = FacturaCompraDetalleForm
