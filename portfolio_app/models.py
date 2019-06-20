from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import reverse
from django.utils import timezone


class Contact(models.Model):
	name = models.CharField(max_length=80)
	email = models.CharField(max_length=80)
	subject = models.CharField(max_length=200)
	message = models.TextField()

	def __str__(self):
		return self.name

	def absolute_url(self):
		return reverse('contact_detail', kwargs={'id': self.pk, })

	def __unicode__(self):
		return self.name


class Tag(models.Model):
	tag_name = models.CharField(max_length=50, unique=True)
	created_at = models.DateTimeField(auto_now_add=True)


	def __str__(self):
		return self.tag_name

	# def get_absolute_url(self):
	# 	return reverse('polls:detail', kwargs={'pk': self.pk, })


class Category(models.Model):
	category_name = models.CharField(max_length=50, unique=True)
	created_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.category_name


class Blog(models.Model):
	STATUS_CHOICES = (
		('unpublished', 'Unpublished'),
		('published', 'Published'),
	)
	title = models.CharField(max_length=250)
	tag = models.ManyToManyField(Tag)
	category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='blogs')
	feature_image = models.ImageField(upload_to='blog_images/%Y/%m/%d', blank=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='unpublished')
	blog_view_count = models.IntegerField(default=0)

	def __str__(self):
		return self.title

	class Meta:
		ordering = ('-created_at',)

#User portfolio
class Portfolio(models.Model):
	author = models.CharField(max_length = 100)
	description = models.TextField()
	image = models.ImageField(upload_to ='portfolioImage',blank = True, null = True)
	published_at = models.DateTimeField(auto_now_add = True)

	def __str__(self):
		return self.author

	def get_absolute_url(self):
		return reverse('portfolio:portfolio')

#User project
class Project(models.Model):
	portfolio = models.ManyToManyField(Portfolio)
	title = models.CharField(max_length = 150)
	description = models.TextField()
	image = models.ImageField(upload_to='ProjectImage', blank=True, null=True)
	started_at = models.DateTimeField(blank=False, null=False)
	completed_at = models.DateTimeField(default=timezone.now)


	def __str__(self):
		return '%s' %(self.title)

	def get_absolute_url(self):
		return reverse('portfolio:project')
