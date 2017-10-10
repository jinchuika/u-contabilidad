from django import forms

from bancos.models import Banco, CuentaBanco

class BancoForm(forms.ModelForm):
    class Meta:
        model = Banco
        fields = '__all__'


class CuentaBancoForm(forms.ModelForm):
    class Meta:
        model = CuentaBanco
        fields = ('titular',)
    