from django.db import models
from django.urls import reverse_lazy

from bancos.models import Cheque
from inventario.models import Producto
from contabilidad.models import CuentaContable


class TipoProveedor(models.Model):

    """Indica si un proveedor es persona individual, empresa, etc.
    
    Attributes:
        tipo_proveedor (str): Nombre a mostrar
    """
    
    tipo_proveedor = models.CharField(max_length=15)

    class Meta:
        verbose_name = "Tipo de proveedor"
        verbose_name_plural = "Tipos de proveedor"

    def __str__(self):
        return self.tipo_proveedor


class Proveedor(models.Model):

    """Proveedor para factura.
    
    Attributes:
        nit (str): NIT del proveedor
        nombre (str): Nombre a mostrar
        tipo_proveedor (:class:`TipoProveedor`): Tipo de proveedor
    """
    
    nit = models.CharField(max_length=10, unique=True)
    nombre = models.CharField(max_length=128)
    tipo_proveedor = models.ForeignKey(
        TipoProveedor,
        on_delete=models.PROTECT,
        verbose_name='Tipo de proveedor')
    telefono = models.PositiveIntegerField(
        null=True,
        blank=True,
        verbose_name='Teléfono')
    direccion = models.TextField(
        null=True,
        blank=True,
        verbose_name='Dirección')

    class Meta:
        verbose_name = "Proveedor"
        verbose_name_plural = "Proveedores"

    def __str__(self):
        return self.nombre

    def get_absolute_url(self):
        return reverse_lazy('proveedor_detail', kwargs={'pk': self.id})


class FacturaCompra(models.Model):

    """Factura para registrar una compra de mercadería, inventario o servicio
    
    Attributes:
        fecha_emision (date): Fecha en la que se emitió la factura
        fecha_vencimiento (date): Fecha en la que debe pagarse la factura
        numero (int): Número de factura
        proveedor (:class:`Proveedor`): Proveedor del producto
        serie (str): Serie de la factura
    """
    
    proveedor = models.ForeignKey(Proveedor, on_delete=models.PROTECT)
    serie = models.CharField(max_length=12, null=True, blank=True)
    numero = models.PositiveIntegerField(verbose_name='Número')
    fecha_emision = models.DateField()
    fecha_vencimiento = models.DateField()
    completa = models.BooleanField(default=False, blank=True)

    class Meta:
        verbose_name = "Factura"
        verbose_name_plural = "Facturas"
        unique_together = ('proveedor', 'serie', 'numero')

    def __str__(self):
        return '{proveedor} - {serie}{numero}'.format(
            proveedor=self.proveedor,
            serie=self.serie,
            numero=self.numero)

    def get_absolute_url(self):
        return reverse_lazy('factura_detail', kwargs={'pk': self.id})

    @property
    def total(self):
        return sum(detalle.cantidad * detalle.precio_unitario for detalle in self.detalles.all())

    @property
    def pagado(self):
        return sum(pago.monto for pago in self.pagos.all())

    @property
    def saldo(self):
        return self.total - self.pagado

    @property
    def pagada(self):
        return self.total > self.pagado


class FacturaCompraDetalle(models.Model):

    """Detalle de una factura de compra
    
    Attributes:
        cantidad (int): Cantidad de producto comprado
        cuenta_contable (:class:`CuentaContable`): Cuenta a la cual está relacionada la compra de este producto
        factura (:class:`FacturaCompra`): Factura  la que pertenece el detalle
        precio_unitario (date): Precio unitario del producto
        producto (:class:`Producto`): Producto comprado
    """
    
    factura = models.ForeignKey(
        FacturaCompra,
        on_delete=models.PROTECT,
        related_name='detalles')
    producto = models.ForeignKey(
        Producto,
        on_delete=models.PROTECT,
        related_name='compras')
    cantidad = models.PositiveIntegerField(default=1)
    precio_unitario = models.DecimalField(
        max_digits=8,
        decimal_places=2)
    cuenta_contable = models.ForeignKey(
        CuentaContable,
        on_delete=models.PROTECT)

    class Meta:
        verbose_name = "Detalle de factura"
        verbose_name_plural = "Detalles de factura"

    def __str__(self):
        return '{} - {}'.format(
            self.factura.numero,
            self.producto)

    @property
    def subtotal(self):
        return self.precio_unitario * self.cantidad


class Pago(models.Model):
    factura = models.ForeignKey(FacturaCompra, related_name='pagos')
    cheque = models.ForeignKey(Cheque)
    fecha = models.DateField()

    class Meta:
        verbose_name = "Pago"
        verbose_name_plural = "Pagos"

    def __str__(self):
        return '{factura} - {monto}'.format(
            factura=self.factura,
            monto=self.cheque.monto)

    @property
    def monto(self):
        return self.cheque.monto
