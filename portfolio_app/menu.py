from django.utils.translation import ugettext_lazy as _
from django.utils.safestring import mark_safe

from menus.base import NavigationNode
from menus.menu_pool import menu_pool
from cms.menu_bases import CMSAttachMenu

from .models import Contact

class PortfolioSubMenu(CMSAttachMenu):
    name = _("Portfolio Sub-Menu")

    def get_nodes(self, request):
        nodes = []
        for c in Contact.objects.all():
            node = NavigationNode(mark_safe(c.name), c.absolute_url(), c.id,)
            nodes.append(node)
        return nodes

menu_pool.register_menu(PortfolioSubMenu)
