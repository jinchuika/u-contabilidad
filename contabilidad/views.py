from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import DetailView, ListView, TemplateView
from django.views.generic.edit import CreateView, UpdateView, FormView

from braces.views import LoginRequiredMixin

from pagos.models import FacturaCompra
from contabilidad.models import CuentaContable


class HomeView(LoginRequiredMixin, TemplateView):
    template_name = "contabilidad/dashboard.html"


class CuentaContableCreateView(LoginRequiredMixin, CreateView):
    model = CuentaContable
    fields = '__all__'


class CuentaContableListView(LoginRequiredMixin, ListView):
    model = CuentaContable


class CuentaContableDetailView(LoginRequiredMixin, DetailView):
    model = CuentaContable


class FacturaPendienteListView(ListView):
    template_name = "contabilidad/cuentas_pendientes.html"
    context_object_name = 'pendientes_list'

    def get_queryset(self):
        no_pagadas = []
        queryset = FacturaCompra.objects.all()
        for factura in queryset:
            if factura.pagada:
                no_pagadas.append(factura.id)
        return queryset.exclude(id__in=no_pagadas)

    def get_context_data(self, **kwargs):
        context = super(FacturaPendienteListView, self).get_context_data(**kwargs)
        return context


class UserListView(LoginRequiredMixin, ListView):
    template_name = 'contabilidad/user_list.html'
    model = User


class UserCreateVIew(LoginRequiredMixin, FormView):
    form_class = UserCreationForm
    template_name = 'contabilidad/user_form.html'
    success_url = reverse_lazy('user_list')

    def form_valid(self, form):
        form.save()
        return super(UserCreateVIew, self).form_valid(form)
