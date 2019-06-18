from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from .models import PortfolioPluginModel
from django.utils.translation import ugettext as _


@plugin_pool.register_plugin  # register the plugin
class PollPluginPublisher(CMSPluginBase):
    model = PortfolioPluginModel  # model where plugin data are saved
    module = _("Portfolio")
    name = _("Portfolio Plugin")  # name of the plugin in the interface
    render_template = "portfolio_cms_integration/portfolio_plugin.html"

    def render(self, context, instance, placeholder):
        context.update({'instance': instance})
        return context