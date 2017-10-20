# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-18 14:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contabilidad', '0001_initial'),
        ('inventario', '0001_initial'),
        ('bancos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FacturaCompra',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serie', models.CharField(blank=True, max_length=12, null=True)),
                ('numero', models.PositiveIntegerField(verbose_name='Número')),
                ('fecha_emision', models.DateField()),
                ('fecha_vencimiento', models.DateField()),
                ('completa', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Factura',
                'verbose_name_plural': 'Facturas',
            },
        ),
        migrations.CreateModel(
            name='FacturaCompraDetalle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.PositiveIntegerField(default=1)),
                ('precio_unitario', models.DecimalField(decimal_places=2, max_digits=8)),
                ('cuenta_contable', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='contabilidad.CuentaContable')),
                ('factura', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='detalles', to='pagos.FacturaCompra')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='compras', to='inventario.Producto')),
            ],
            options={
                'verbose_name': 'Detalle de factura',
                'verbose_name_plural': 'Detalles de factura',
            },
        ),
        migrations.CreateModel(
            name='Pago',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField(default=django.utils.timezone.now)),
                ('cheque', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pagos', to='bancos.Cheque')),
                ('factura', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pagos', to='pagos.FacturaCompra')),
            ],
            options={
                'verbose_name': 'Pago',
                'verbose_name_plural': 'Pagos',
            },
        ),
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nit', models.CharField(max_length=10, unique=True)),
                ('nombre', models.CharField(max_length=128)),
                ('telefono', models.PositiveIntegerField(blank=True, null=True, verbose_name='Teléfono')),
                ('direccion', models.TextField(blank=True, null=True, verbose_name='Dirección')),
            ],
            options={
                'verbose_name': 'Proveedor',
                'verbose_name_plural': 'Proveedores',
            },
        ),
        migrations.CreateModel(
            name='TipoProveedor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_proveedor', models.CharField(max_length=15)),
            ],
            options={
                'verbose_name': 'Tipo de proveedor',
                'verbose_name_plural': 'Tipos de proveedor',
            },
        ),
        migrations.AddField(
            model_name='proveedor',
            name='tipo_proveedor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='pagos.TipoProveedor', verbose_name='Tipo de proveedor'),
        ),
        migrations.AddField(
            model_name='facturacompra',
            name='proveedor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='pagos.Proveedor'),
        ),
        migrations.AlterUniqueTogether(
            name='facturacompra',
            unique_together=set([('proveedor', 'serie', 'numero')]),
        ),
    ]
