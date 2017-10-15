from django.views.generic import DetailView, ListView, TemplateView
from django.views.generic.edit import CreateView, UpdateView

from braces.views import LoginRequiredMixin

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
