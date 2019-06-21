from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from .models import PortfolioPluginModel, ProjectPluginModel, TestimonialPluginModel, BlogPluginModel
from django.utils.translation import ugettext as _
from .models import Portfolio, Project, Testimonial, Blog


@plugin_pool.register_plugin  # register the plugin
class PortfolioPluginPublisher(CMSPluginBase):
    model = PortfolioPluginModel  # model where plugin data are saved
    module = _("Portfolio")
    name = _("Portfolio Plugin")  # name of the plugin in the interface
    render_template = "portfolio_cms_integration/portfolio_plugin.html"

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


@plugin_pool.register_plugin  # register the plugin
class TestimonialPluginPublisher(CMSPluginBase):
    model = TestimonialPluginModel  # model where plugin data are saved
    module = _("Testimonial")
    name = _("Testimonial Plugin")  # name of the plugin in the interface
    render_template = "portfolio_cms_integration/testimonial_plugin.html"

    def render(self, context, instance, placeholder):
        testimonial = Testimonial.objects.all()
        context.update({'instance': instance, 'testimonial':testimonial})
        return context


@plugin_pool.register_plugin  # register the plugin
class BlogPluginPublisher(CMSPluginBase):
    model = BlogPluginModel  # model where plugin data are saved
    module = _("Blog")
    name = _("Blog Plugin")  # name of the plugin in the interface
    render_template = "portfolio_cms_integration/blog_plugin.html"

    def render(self, context, instance, placeholder):
        blogs = Blog.objects.all()
        context.update({'instance': instance, 'blogs':blogs})
        return context