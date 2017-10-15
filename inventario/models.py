from datetime import datetime, timedelta
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

    def saldo(self, fecha=datetime.today()):
        annos = (fecha.year - self.fecha_registro.year) * 12
        meses = annos + fecha.month - self.fecha_registro.month
        depreciacion = (self.depreciacion / 12) * meses
        monto = self.precio - (self.precio * depreciacion)
        if depreciacion >= 1:
            depreciacion = 1
        if monto <= 0:
            monto = 0
        return {
            'monto': monto,
            'mes': meses,
            'depreciado': depreciacion}

    def historico(self):
        respuesta = []
        fecha = datetime.today()
        saldo = self.saldo()
        while saldo['mes'] > 0:
            fecha = fecha - timedelta(days=30)
            saldo = self.saldo(fecha)
            respuesta.append(saldo)
        return respuesta
