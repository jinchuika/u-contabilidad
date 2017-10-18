from django import forms

from bancos.models import Cheque
from bancos.forms import ChequeForm
from pagos.models import FacturaCompra, FacturaCompraDetalle


class FacturaCompraForm(forms.ModelForm):
    class Meta:
        model = FacturaCompra
        fields = '__all__'
        exclude = ('completa',)


class FacturaCompraCompletaForm(forms.ModelForm):
    class Meta:
        model = FacturaCompra
        fields = ('completa',)
        widgets = {
            'completa': forms.HiddenInput()
        }


class FacturaCompraDetalleForm(forms.ModelForm):
    class Meta:
        model = FacturaCompraDetalle
        fields = "__all__"
        widgets = {
            'factura': forms.HiddenInput()
        }


class PagoForm(ChequeForm):
    factura = forms.ModelChoiceField(
        queryset=FacturaCompra.objects.all(),
        widget=forms.HiddenInput())

    def __init__(self, *args, **kwargs):
        monto_maximo = kwargs.pop('monto_maximo', False)
        fecha_minima = kwargs.pop('fecha_minima', False)
        super(PagoForm, self).__init__(*args, **kwargs)
        if monto_maximo:
            self.fields['monto'].widget = forms.NumberInput(attrs={
                'min': 0.01,
                'max': monto_maximo,
                'step': 0.01})
        if fecha_minima:
            self.fields['fecha'].widget = forms.DateInput(attrs={
                'max': str(fecha_minima),
                'class': 'datepicker'})
