from django.db import models
from cms.models import CMSPlugin
from portfolio_app.models import Portfolio, Project


class PortfolioPluginModel(CMSPlugin):
	portfolio = models.ManyToManyField(Portfolio)
	# title = models.CharField(max_length = 150)


	# def __str__(self):
	# 	return self.title

class ProjectPluginModel(CMSPlugin):
	author = models.ManyToManyField(Project)