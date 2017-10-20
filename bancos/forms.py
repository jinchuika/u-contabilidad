from django import forms
from django.db.models import Sum, Count, F

from bancos.models import Banco, CuentaBanco, Chequera, Cheque, DepositoBanco

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
        queryset=Chequera.objects.all())

    class Meta:
        model = Cheque
        fields = '__all__'
        exclude = ('numero',)
        widgets = {
            'monto': forms.NumberInput(attrs={'min': 0.01})
        }


class DepositoBancoForm(forms.ModelForm):
    class Meta:
        model = DepositoBanco
        fields = '__all__'
        widgets = {
            'cuenta': forms.Select(attrs={'class': 'select2'}),
            'fecha': forms.TextInput(attrs={'class': 'datepicker'}),
            'monto': forms.NumberInput(attrs={'min': 0.01})
        }