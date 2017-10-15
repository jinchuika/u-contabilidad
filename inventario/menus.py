from menu import Menu
from conta.menus import ViewMenuItem

from django.core.urlresolvers import reverse_lazy

# Contabilidad
contabilidad_children = (
    ViewMenuItem(
        "Cuentas contables",
        reverse_lazy('cuentacontable_list'),
        weight=10,
        icon="fa-desktop"),)

Menu.add_item(
    "user",
    ViewMenuItem(
        "Contabilidad",
        '#',
        weight=40,
        icon="fa-cog",
        children=contabilidad_children))
