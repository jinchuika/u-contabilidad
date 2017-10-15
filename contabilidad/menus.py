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
        icon="fa-desktop"),)

Menu.add_item(
    "user",
    ViewMenuItem(
        "Contabilidad",
        '#',
        weight=40,
        icon="fa-cog",
        children=contabilidad_children))

# Menú de bancos
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
