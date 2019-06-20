from django.urls import reverse
from django.utils.translation import ugettext_lazy as _

from cms.menu_bases import CMSAttachMenu
from menus.base import NavigationNode
from menus.menu_pool import menu_pool

from portfolio_app.models import Portfolio


class PortfolioMenu(CMSAttachMenu):
    name = _("Portfolio Menu")  # give the menu a name this is required.

    def get_nodes(self, request):
        """
        This method is used to build the menu tree.
        """
        nodes = []
        for portfolio in Portfolio.objects.all():
            node = NavigationNode(
                title=portfolio.author,
                url=reverse('portfolio:portfolio'),
                id=portfolio.pk,  # unique id for this node within the menu
            )
            nodes.append(node)
        return nodes

menu_pool.register_menu(PortfolioMenu)