from django.db import models
from django.urls import reverse_lazy


class CuentaContable(models.Model):

    """Cuenta para llevar el registro contable del a empresa
    
    Attributes:
        activo_fijo (bool): Indica si la cuenta corresponde a un activo fijo
        depreciacion (float): Indica el valor de la depreciación en caso de que exista
        nombre (str): El nombre de la cuenta
    """

    nombre = models.CharField(max_length=128)
    depreciacion = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        default=0.0,
        verbose_name='Depreciación')
    activo_fijo = models.BooleanField()

    class Meta:
        verbose_name = "Cuenta contable"
        verbose_name_plural = "Cuentas contables"

    def __str__(self):
        return self.nombre

    def get_absolute_url(self):
        return reverse_lazy('cuentacontable_detail', kwargs={'pk': self.id})
