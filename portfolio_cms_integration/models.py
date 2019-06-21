from django.db import models
from cms.models import CMSPlugin
from portfolio_app.models import Portfolio, Project


class PortfolioPluginModel(CMSPlugin):
	portfolio = models.ManyToManyField(Portfolio)

	# def copy_relations(self, oldinstance):
	# 	for p in oldinstance.portfolio.all():
	# 		# instance.pk = None; instance.pk.save() is the slightly odd but
	# 		# standard Django way of copying a saved model instance
	# 		p.pk = None
	# 		p.plugin = self
	# 		p.save()

	# def copy_relations(self, oldinstance):
	# 	self.portfolio = oldinstance.portfolio.all()


class ProjectPluginModel(CMSPlugin):
	author = models.ManyToManyField(Project)