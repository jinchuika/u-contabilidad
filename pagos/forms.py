from django import forms

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
    