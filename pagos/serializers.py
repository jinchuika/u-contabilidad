from datetime import date
from rest_framework import serializers

from pagos.models import FacturaCompra

class FacturaCompraSerializer(serializers.ModelSerializer):
    proveedor = serializers.StringRelatedField()
    saldo = serializers.DecimalField(max_digits=8, decimal_places=2)
    dias = serializers.SerializerMethodField()

    class Meta:
        model = FacturaCompra
        fields = [
        'proveedor',
        'saldo',
        'dias',
        'fecha_vencimiento'
        ]

    def get_dias(self, obj):
        dias = (obj.fecha_vencimiento - date.today()).days
        if dias < 0:
            return 'Vencida'
        elif 0 < dias < 30:
            return '30'
        elif 30 < dias < 60:
            return '60'
        elif 66 < dias < 90:
            return '90'
        else:
            return '> 90'

