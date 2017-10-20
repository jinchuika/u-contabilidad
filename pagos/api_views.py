from rest_framework import viewsets

from pagos.models import FacturaCompra
from pagos.serializers import FacturaCompraSerializer

class FacturaCompraViewSet(viewsets.ModelViewSet):
    serializer_class = FacturaCompraSerializer
    
    def get_queryset(self):
        no_pagadas = []
        queryset = FacturaCompra.objects.all()
        for factura in queryset:
            if factura.pagada:
                no_pagadas.append(factura.id)
        return queryset.exclude(id__in=no_pagadas)
