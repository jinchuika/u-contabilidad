from django.db import models
from django.urls import reverse_lazy


class Banco(models.Model):

    """Banco para generar cuentas bancarias
    
    Attributes:
        activo (bool): Indica que puedan realizarse operaciones
        nombre (str): Nombre para identificar al banco
    """
    
    nombre = models.CharField(max_length=128)
    activo = models.BooleanField(blank=True)

    class Meta:
        verbose_name = "Banco"
        verbose_name_plural = "Bancos"

    def __str__(self):
        return self.nombre

    def get_absolute_url(self):
        return reverse_lazy('banco_detail', kwargs={'pk': self.id})

    @property
    def cantidad_chequeras(self):
        return sum(cuenta.chequeras.count() for cuenta in self.cuentas.all())


class CuentaBancoTipo(models.Model):

    """Tipo de cuenta bancaria. Se usa para diferenciar aquellas
    que no pueden hacer retiros (como las de inversión).
    
    Attributes:
        puede_retirar (bool): Indica si esta cuenta puede hacer retiros o no
        tipo (str): El nombre del tipo de cuenta
    """
    
    tipo = models.CharField(max_length=20)
    puede_retirar = models.BooleanField(default=True, blank=True)

    class Meta:
        verbose_name = "Tipo de cuenta bancaria"
        verbose_name_plural = "Tipos de cuenta bancaria"

    def __str__(self):
        return self.tipo


class CuentaBanco(models.Model):

    """Una cuenta bancaria para utilizar en la organización.
    
    Attributes:
        banco (:class:`Banco`): El banco al que pertenece esta cuenta
        numero (str): El número de cuenta bancaria provisto por el banco.
        tipo (:class:`CuentaBancoTipo`): Tipo de cuenta bancaria
        titular (str): Nombre del titular de la cuenta
    """
    
    banco = models.ForeignKey(Banco, related_name='cuentas')
    tipo = models.ForeignKey(CuentaBancoTipo)
    numero = models.CharField(max_length=20)
    titular = models.CharField(max_length=128)

    class Meta:
        verbose_name = "Cuenta bancaria"
        verbose_name_plural = "Cuentas bancarias"

    def __str__(self):
        return '{numero} ({banco})'.format(
            numero=self.numero,
            banco=self.banco)

    def get_absolute_url(self):
        return reverse_lazy('cuenta_detail', kwargs={'pk': self.id})

    @property
    def credito(self):
        return sum(deposito.monto for deposito in self.depositos.all())

    @property
    def debito(self):
        return sum(cheque.monto for cheque in Cheque.objects.filter(chequera__cuenta=self))

    @property
    def saldo(self):
        return self.credito - self.debito


class ChequeraManager(models.Manager):
    def get_queryset(self):
        no_disponibles = []
        queryset = super().get_queryset()
        for chequera in queryset:
            if chequera.cheques_disponibles <= 0:
                no_disponibles.append(chequera.id)
        return queryset.exclude(id__in=no_disponibles)

class Chequera(models.Model):

    """Chequera relacionada a una cuenta bancaria.

    Attributes:
        cantidad_cheques (int): Cantidad de cheques que puede emitir esta chequera
        cuenta (:class:`CuentaBanco`): Cuenta bancaria que emite esta chequera :class:`CuentaBancaria`.
        numero (int): Número de chequera
    """

    cuenta = models.ForeignKey(CuentaBanco, related_name='chequeras')
    numero = models.CharField(max_length=20)
    cantidad_cheques = models.IntegerField(default=1)

    objects = models.Manager()
    disponibles = ChequeraManager()

    class Meta:
        verbose_name = "Chequera"
        verbose_name_plural = "Chequeras"
        unique_together = ('cuenta', 'numero')

    def __str__(self):
        return '{numero} - {banco}'.format(
            numero=self.numero,
            banco=self.cuenta.banco)

    def get_absolute_url(self):
        return reverse_lazy('chequera_detail', kwargs={'pk': self.id})

    @property
    def cheques_disponibles(self):
        return self.cantidad_cheques - self.cheques.count()


class Cheque(models.Model):

    """Cheque para efectuar pagos
    
    Attributes:
        chequera (:class:`Chequera`): Chequera que emite el banco
        fecha (date): Fecha en la que se crea el cheque
        monto (float): Cantidad de dinero a pagar
        nombre (str): Nombre de la persona para quien se emite el cheque
        numero (int): Número de cheque
    """

    chequera = models.ForeignKey(Chequera, related_name='cheques')
    numero = models.PositiveIntegerField(verbose_name='Número')
    fecha = models.DateField()
    nombre = models.CharField(max_length=128, verbose_name='A nombre de')
    monto = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        verbose_name = "Cheque"
        verbose_name_plural = "Cheques"
        unique_together = ('chequera', 'numero')

    def __str__(self):
        return '{numero} - {cuenta}'.format(
            numero=self.numero,
            cuenta=self.chequera.cuenta)


class DepositoBanco(models.Model):

    """Registro para añadir dinero a una :class:`CuentaBanco`.
    
    Attributes:
        comentario (str): Observaciones para el depósito
        cuenta (:class:`CuentaBanco`): La cuenta a la que se deposita
        fecha (date): Fecha del registro
        monto (float): Cantidad a depositar
    """
    
    cuenta = models.ForeignKey(CuentaBanco, related_name='depositos')
    fecha = models.DateField()
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    comentario = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = "Depósito bancario"
        verbose_name_plural = "Depósitos bancarios"

    def __str__(self):
        return '{fecha} - {cuenta}'.format(
            fecha=self.fecha,
            cuenta=self.cuenta.numero)
