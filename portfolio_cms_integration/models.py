from django.db import models
from cms.models import CMSPlugin
from portfolio_app.models import Portfolio, Project, Testimonial, Blog


class PortfolioPluginModel(CMSPlugin):
	portfolio = models.ManyToManyField(Portfolio)

	def copy_relations(self, oldinstance):
		self.portfolio.set(oldinstance.portfolio.all())


class ProjectPluginModel(CMSPlugin):
	project = models.ManyToManyField(Project)

	def copy_relations(self, oldinstance):
		self.project.set(oldinstance.project.all())


class TestimonialPluginModel(CMSPlugin):
	testimonial = models.ManyToManyField(Testimonial)

	def copy_relations(self, oldinstance):
		self.testimonial.set(oldinstance.testimonial.all())


class BlogPluginModel(CMSPlugin):
	blog = models.ManyToManyField(Blog)

	def copy_relations(self, oldinstance):
		self.blog.set(oldinstance.blog.all())