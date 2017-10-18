from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, UpdateView

from braces.views import LoginRequiredMixin

from inventario.models import Producto, ActivoFijo


class ProductoCreateView(LoginRequiredMixin, CreateView):
    model = Producto
    fields = '__all__'


class ProductoDetailView(LoginRequiredMixin, DetailView):
    model = Producto


class ProductoListView(LoginRequiredMixin, ListView):
    model = Producto


class ActivoFijoListView(LoginRequiredMixin, ListView):
    model = ActivoFijo


class ActivoFijoDetailView(LoginRequiredMixin, DetailView):
    model = ActivoFijo
