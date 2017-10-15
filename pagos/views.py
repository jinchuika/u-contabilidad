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
            context['detalle_form'] = FacturaCompraDetalleForm(initial={
            'factura': self.object})
        context['completa_form'] = FacturaCompraCompletaForm(
            instance=self.object,
            initial={'completa': True})
        if self.object.completa:
            context['cheque_form'] = PagoForm(
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
        context['facturacompra'] = FacturaCompra.objects.get(id=self.kwargs['pk'])
        return context


# class PagoCreateView(CreateView):
#     model = Cheque
#     form_class = PagoForm

#     def form_valid(self, form):
#         self.object = form.save(commit=False)
#         self.object.save()
#         pago = Pago(cheque=self.object, factura=form.cleaned_data['factura'])
#         pago.save()
#         return super(PagoCreateView, self).form_valid(form)
