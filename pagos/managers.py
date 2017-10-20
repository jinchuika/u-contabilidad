from datetime import timedelta, date
from django.db import models


class PendientesManager(models.QuerySet):
    def get_queryset(self):
        no_pagadas = []
        queryset = super().get_queryset()
        for factura in queryset:
            if factura.pagada:
                no_pagadas.append(factura.id)
        return queryset.exclude(id__in=no_pagadas)

    def vencidas(self):
        return self.filter(fecha_vencimiento__lt=date.today())

    def a_30(self):
        td = date.today() + timedelta(days=30)
        return self.get_queryset().filter(fecha_vencimiento__range=[date.today(), td])

    def a_60(self):
        minimo = date.today() + timedelta(days=31)
        maximo = date.today() + timedelta(days=60)
        return self.get_queryset().filter(fecha_vencimiento__range=[minimo, maximo])

    def a_90(self):
        minimo = date.today() + timedelta(days=61)
        maximo = date.today() + timedelta(days=90)
        return self.get_queryset().filter(fecha_vencimiento__range=[minimo, maximo])

    def mas_90(self):
        minimo = date.today() + timedelta(days=90)
        return self.get_queryset().filter(fecha_vencimiento__gt=minimo)
