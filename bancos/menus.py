from menu import Menu
from conta.menus import ViewMenuItem

from django.core.urlresolvers import reverse_lazy


# Bancos
bancos_children = (
    ViewMenuItem(
        "Bancos",
        reverse_lazy("banco_list"),
        weight=10,
        icon="fa-list"),
    ViewMenuItem(
        "Cuentas bancarias",
        reverse_lazy("cuenta_list"),
        weight=5,
        icon="fa-list"))

Menu.add_item(
    "user",
    ViewMenuItem(
        "Bancos",
        '#',
        weight=20,
        icon="fa-leaf",
        children=bancos_children))
