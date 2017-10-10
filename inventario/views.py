from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, UpdateView

from inventario.models import Producto, ActivoFijo


class ProductoCreateView(CreateView):
    model = Producto
    fields = '__all__'


class ProductoDetailView(DetailView):
    model = Producto


class ProductoListView(ListView):
    model = Producto


class ActivoFijoListView(ListView):
    model = ActivoFijo
