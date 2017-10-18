from django import forms
from django.db.models import Sum, Count, F

from bancos.models import Banco, CuentaBanco, Chequera, Cheque

class BancoForm(forms.ModelForm):
    class Meta:
        model = Banco
        fields = '__all__'


class CuentaBancoForm(forms.ModelForm):
    class Meta:
        model = CuentaBanco
        fields = ('titular',)


class ChequeForm(forms.ModelForm):
    chequera = forms.ModelChoiceField(
        queryset=Chequera.disponibles.all())

    class Meta:
        model = Cheque
        fields = '__all__'
        exclude = ('numero',)
        widgets = {
            'monto': forms.NumberInput(attrs={'min': 0.01})
        }
