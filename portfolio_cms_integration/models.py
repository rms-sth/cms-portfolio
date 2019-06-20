from django.db import models
from cms.models import CMSPlugin
from portfolio_app.models import Portfolio, Project
from django.utils import timezone
from cms.plugin_base import CMSPluginBase

class PortfolioPluginModel(CMSPlugin):
	# model = Portfolio
	# name = _("Portfolio Plugin")
	# render_template = "hello_plugin.html"
	# cache = False
	portfolio = models.ManyToManyField(Portfolio)
	# # project = models.ManyToManyField(Portfolio)
	# title = models.CharField(max_length = 150)
	# description = models.TextField()
	# image = models.ImageField(upload_to='ProjectImage', blank=True, null=True)
	# started_at = models.DateTimeField(blank=False, null=False)
	# completed_at = models.DateTimeField(default=timezone.now)
	# # title = models.CharField(max_length = 150)


	# def __str__(self):
	# 	return self.portfolio

class ProjectPluginModel(CMSPlugin):
	author = models.ManyToManyField(Project)