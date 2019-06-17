from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool
from django.utils.translation import ugettext_lazy as _

from . menu import PortfolioSubMenu

class PortfolioApp(CMSApp):
    name = _('Portfolio')
    urls = ['portfolio_app.urls']
    app_name = 'portfolio' #optional
    menus = [PortfolioSubMenu, ]

apphook_pool.register(PortfolioApp)
