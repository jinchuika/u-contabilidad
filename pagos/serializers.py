from datetime import date
from rest_framework import serializers

from pagos.models import FacturaCompra

class FacturaCompraSerializer(serializers.ModelSerializer):
    proveedor = serializers.StringRelatedField()
    total = serializers.DecimalField(max_digits=8, decimal_places=2)
    dias = serializers.SerializerMethodField()

    class Meta:
        model = FacturaCompra
        fields = '__all__'

    def get_dias(self, obj):
        return (obj.fecha_vencimiento - date.today()).days
