from django.db import models
from cms.models import CMSPlugin
from portfolio_app.models import Portfolio


class PortfolioPluginModel(CMSPlugin):
	portfolio = models.ManyToManyField(Portfolio)

	def __str__(self):
		return self.portfolio.author