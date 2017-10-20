from menu import Menu, MenuItem
from django.core.urlresolvers import reverse_lazy


class ViewMenuItem(MenuItem):
    def __init__(self, *args, **kwargs):
        super(ViewMenuItem, self).__init__(*args, **kwargs)
        if 'perm' in kwargs:
            self.perm = kwargs.pop('perm')

    def check(self, request):
        """ Revisa por grupo """
        if hasattr(self, 'group'):
            if request.user.groups.filter(name=self.group).exists():
                self.visible = True
                return True
            else:
                self.visible = False
        """ Revisa los permisos """
        if hasattr(self, 'perm'):
            if request.user.has_perm(self.perm):
                self.visible = True
                return True
            else:
                self.visible = False

# Contabilidad
contabilidad_children = (
    ViewMenuItem(
        "Cuentas contables",
        reverse_lazy('cuentacontable_list'),
        weight=10,
        icon="fa-desktop"),
    ViewMenuItem(
        "Cuentas por pagar",
        reverse_lazy('cuentas_por_pagar'),
        weight=10,
        icon="fa-clock-o"))

Menu.add_item(
    "user",
    ViewMenuItem(
        "Contabilidad",
        '#',
        weight=40,
        icon="fa-list-alt",
        children=contabilidad_children))

# Menú de bancos
bancos_children = (
    ViewMenuItem(
        "Listado de bancos",
        reverse_lazy("banco_list"),
        weight=10,
        icon="fa-list"),
    ViewMenuItem(
        "Cuentas bancarias",
        reverse_lazy("cuenta_list"),
        weight=20,
        icon="fa-address-card-o"),
    ViewMenuItem(
        "Nuevo depósito",
        reverse_lazy("deposito_add"),
        weight=20,
        icon="fa-plus"))

Menu.add_item(
    "user",
    ViewMenuItem(
        "Bancos",
        '#',
        weight=20,
        icon="fa-university",
        children=bancos_children))

# Pagos de bancos
pagos_children = (
    ViewMenuItem(
        "Proveedores",
        reverse_lazy("proveedor_list"),
        weight=10,
        icon="fa-user"),
    ViewMenuItem(
        "Nueva compra",
        reverse_lazy("factura_add"),
        weight=5,
        icon="fa-plus"),
    ViewMenuItem(
        "Lista de compras",
        reverse_lazy("factura_list"),
        weight=5,
        icon="fa-list"))

Menu.add_item(
    "user",
    ViewMenuItem(
        "Pagos",
        '#',
        weight=20,
        icon="fa-usd",
        children=pagos_children))


# Inventario
inventario_children = (
    ViewMenuItem(
        "Productos",
        reverse_lazy("producto_list"),
        weight=10,
        icon="fa-cube"),
    ViewMenuItem(
        "Activos fijos",
        reverse_lazy("activofijo_list"),
        weight=5,
        icon="fa-desktop"))

Menu.add_item(
    "user",
    ViewMenuItem(
        "Inventario",
        '#',
        weight=20,
        icon="fa-cubes",
        children=inventario_children))
