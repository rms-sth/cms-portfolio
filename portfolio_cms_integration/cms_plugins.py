from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from .models import PortfolioPluginModel, ProjectPluginModel
from django.utils.translation import ugettext as _
from .models import Portfolio, Project
# from cms.models import CMSPlugin

@plugin_pool.register_plugin  # register the plugin
class PortfolioPluginPublisher(CMSPluginBase):
    model = PortfolioPluginModel  # model where plugin data are saved
    # model = Portfolio(CMSPlugin)
    module = _("Portfolio")
    name = _("Portfolio Plugin")  # name of the plugin in the interface
    render_template = "portfolio_cms_integration/portfolio_plugin.html"
    cache = False

    # def render(self, context, instance, placeholder):
    #     context = super(PortfolioPluginPublisher, self).render(context, instance, placeholder)
    #     return context

    def render(self, context, instance, placeholder):
        port = Portfolio.objects.all()
        context.update({'instance': instance, 'port':port})
        return context


@plugin_pool.register_plugin  # register the plugin
class ProjectPluginPublisher(CMSPluginBase):
    model = ProjectPluginModel  # model where plugin data are saved
    module = _("Project")
    name = _("Project Plugin")  # name of the plugin in the interface
    render_template = "portfolio_cms_integration/project_plugin.html"

    def render(self, context, instance, placeholder):
        project = Project.objects.all()
        context.update({'instance': instance, 'project':project})
        return context