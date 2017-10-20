import random
from datetime import date, timedelta
from contabilidad.models import *
from inventario.models import *
from pagos.models import *
from bancos.models import *

def generar_compras(anno, mes=1):
    prov_count = Proveedor.objects.count()

    for i in range(mes, 12):
        fecha_emision = date(anno, i, i*2)
        fecha_vencimiento = fecha_emision + timedelta(days=((i % 4)+1) * 20)
        FacturaCompra.objects.create(
            numero=i*12,
            fecha_emision=fecha_emision,
            fecha_vencimiento=fecha_vencimiento,
            proveedor=Proveedor.objects.get(pk=random.randint(1, prov_count -1)))
        print(str(i) + " generada " + str(FacturaCompra.objects.last()))


def generar_detalles():
    prod_count = Producto.objects.count()
    conta_count = CuentaContable.objects.count()
    compra_qs = FacturaCompra.objects.filter(completa=False)

    for compra in compra_qs.all():
        for i in range(1, 4):
            compra.detalles.create(
                producto=Producto.objects.get(pk=random.randint(1, prod_count -1)),
                cantidad=i,
                precio_unitario=random.randint(1, i * 2) * 750.00,
                cuenta_contable=CuentaContable.objects.get(pk=random.randint(1, conta_count -1))
                )
        compra.completa = True
        compra.save()
        print("Actualizada " + str(compra.id) + " " + str(compra.total))


def pagar_cuentas(a_pagar=1):
    chqra_count = Chequera.objects.count()

    compra_qs = FacturaCompra.objects.all()
    no_pagadas = []
    for factura in compra_qs:
        if factura.pagada:
            no_pagadas.append(factura.id)
    compra_qs = compra_qs.exclude(id__in=no_pagadas)

    for compra in compra_qs.all():
        chequera = Chequera.objects.get(pk=random.randint(1, chqra_count - 1))
        cheque = Cheque.objects.create(
            chequera=chequera,
            numero=chequera.cheques.count() + 1,
            fecha=compra.fecha_vencimiento,
            nombre=compra.proveedor.nombre,
            monto=compra.saldo / a_pagar)
        print("creado cheque: " + str(cheque))
        compra.pagos.create(cheque=cheque)
        print("pagada compra: " + str(compra))


def generar_depositos(anno=2016):
    i = 0
    for cuenta in CuentaBanco.objects.all():
        i = i + 1
        cuenta.depositos.create(
            fecha=date(anno, (i % 12) + 1, i),
            monto=random.randint(1, i) * 7000,
            comentario="De prueba"
            )
        print("Depositado: " + str(cuenta.depositos.last()))


def actualizar_por_pagar(dias=30):
    compra_qs = FacturaCompra.objects.all()
    no_pagadas = []
    for factura in compra_qs:
        if factura.pagada:
            no_pagadas.append(factura.id)
    compra_qs = compra_qs.exclude(id__in=no_pagadas)

    i = 0

    for compra in compra_qs:
        i += 1
        print("Fecha anterior: " + str(compra.fecha_vencimiento))
        compra.fecha_vencimiento = compra.fecha_vencimiento + timedelta(days=(i % 3 + 1) * dias)
        compra.save()
        print("Fecha nueva: " + str(compra.fecha_vencimiento))
