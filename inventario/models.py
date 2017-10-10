from datetime import datetime
from django.db import models
from django.urls import reverse_lazy


class Producto(models.Model):

    """Producto para inventario o para mercadería a la venta
    
    Attributes:
        nombre (models.CharField): Nombre del producto
    """
    
    nombre = models.CharField(max_length=128)

    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"

    def __str__(self):
        return self.nombre

    def get_absolute_url(self):
        return reverse_lazy('producto_detail', kwargs={'pk': self.id})


class ActivoFijo(models.Model):

    """Activo fijo adquirido por la organización que
    puede tener una depreciación cada cierto tiempo.
    
    Attributes:
        depreciacion (models.DecimalField): Depreciación anual del activo
        fecha_registro (models.DateField): Fecha en la que el activo entra al inventario
        precio (models.DecimalField): Precio al que fue adquirido el activo fijo
        producto (:class:`Producto`): Producto adquirido en el inventario
    """
    
    producto = models.ForeignKey(
        Producto,
        on_delete=models.PROTECT,
        related_name='activos_fijos')
    fecha_registro = models.DateField()
    depreciacion = models.DecimalField(max_digits=5, decimal_places=4)
    precio = models.DecimalField(max_digits=8, decimal_places=2)

    class Meta:
        verbose_name = "Activo fijo"
        verbose_name_plural = "Activos fijos"

    def __str__(self):
        return '{}'.format(self.producto)

    def saldo(self):
        annos = (datetime.today().year - self.fecha_registro.year) * 12
        meses = annos + datetime.today().month - self.fecha_registro.month
        depreciacion = (self.depreciacion / 12) * meses
        print(depreciacion)
        return self.precio - (self.precio * depreciacion)
