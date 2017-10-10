from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, UpdateView

from contabilidad.models import CuentaContable


class CuentaContableCreateView(CreateView):
    model = CuentaContable
    fields = '__all__'


class CuentaContableListView(ListView):
    model = CuentaContable


class CuentaContableDetailView(DetailView):
    model = CuentaContable
