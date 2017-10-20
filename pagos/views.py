from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, UpdateView

from braces.views import LoginRequiredMixin


from bancos.models import Cheque
from pagos.models import (
    Proveedor, FacturaCompra, FacturaCompraDetalle, Pago)
from pagos.forms import (
    FacturaCompraForm, FacturaCompraCompletaForm,
    FacturaCompraDetalleForm, PagoForm)


class ProveedorCreateView(LoginRequiredMixin, CreateView):
    model = Proveedor
    fields = '__all__'


class ProveedorListView(LoginRequiredMixin, ListView):
    model = Proveedor


class ProveedorDetailView(LoginRequiredMixin, DetailView):
    model = Proveedor


class FacturaCompraCreateView(LoginRequiredMixin, CreateView):
    model = FacturaCompra
    form_class = FacturaCompraForm


class FacturaCompraDetailView(LoginRequiredMixin, DetailView):
    model = FacturaCompra
    template_name = 'pagos/facturacompra_update.html'

    def get_context_data(self, **kwargs):
        context = super(FacturaCompraDetailView, self).get_context_data(**kwargs)
        if not self.object.completa:
            context['detalle_form'] = FacturaCompraDetalleForm(
                initial={'factura': self.object})
        context['completa_form'] = FacturaCompraCompletaForm(
            instance=self.object,
            initial={'completa': True})

        if self.object.completa:
            # Si la factura ya está completa, envía el formulario de pago
            context['cheque_form'] = PagoForm(
                monto_maximo=self.object.saldo,
                fecha_minima=self.object.fecha_emision,
                initial={'factura': self.object})
        return context


class FacturaCompraUpdateView(LoginRequiredMixin, UpdateView):
    model = FacturaCompra
    form_class = FacturaCompraCompletaForm
    template_name = 'pagos/facturacompra_update.html'


class FacturaCompraDetalleCreateView(LoginRequiredMixin, CreateView):
    model = FacturaCompraDetalle
    form_class = FacturaCompraDetalleForm


class PagoCreateView(LoginRequiredMixin, CreateView):
    model = Pago
    template_name = "pagos/facturacompra_form.html"
    form_class = PagoForm

    def get_context_data(self, **kwargs):
        context = super(PagoCreateView, self).get_context_data(**kwargs)
        return context

    def form_valid(self, form):
        form.instance.numero = form.instance.chequera.cheques.count() + 1
        self.object = form.save()
        self.object.pagos.create(factura=form.cleaned_data['factura'])
        return super(PagoCreateView, self).form_valid(form)

    def get_success_url(self):
        if self.object.pagos.first().factura.pagada:
            return reverse_lazy('home')
        else:
            return self.object.pagos.first().factura.get_absolute_url()


class FacturaCompraListView(ListView):
    model = FacturaCompra
