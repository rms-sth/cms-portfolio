from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from .models import PortfolioPluginModel, ProjectPluginModel
from django.utils.translation import ugettext as _


@plugin_pool.register_plugin  # register the plugin
class PortfolioPluginPublisher(CMSPluginBase):
    model = PortfolioPluginModel  # model where plugin data are saved
    module = _("Portfolio")
    name = _("Portfolio Plugin")  # name of the plugin in the interface
    render_template = "portfolio_cms_integration/portfolio_plugin.html"

    def render(self, context, instance, placeholder):
        context.update({'instance': instance})
        return context


@plugin_pool.register_plugin  # register the plugin
class ProjectPluginPublisher(CMSPluginBase):
    model = ProjectPluginModel  # model where plugin data are saved
    module = _("Project")
    name = _("Project Plugin")  # name of the plugin in the interface
    render_template = "portfolio_cms_integration/project_plugin.html"

    def render(self, context, instance, placeholder):
        context.update({'instance': instance})
        return context