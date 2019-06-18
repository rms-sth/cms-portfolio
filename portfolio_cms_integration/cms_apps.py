from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool


@apphook_pool.register  # register the application
class PortfolioApphook(CMSApp):
    app_name = "portfolio"
    name = "Portfolio Application"

    def get_urls(self, page=None, language=None, **kwargs):
        return ["portfolio_app.urls"]