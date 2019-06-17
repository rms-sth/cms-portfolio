from django.db import models
from django.contrib.auth.models import User


class Contact(models.Model):
	name = models.CharField(max_length=80)
	email = models.CharField(max_length=80)
	subject = models.CharField(max_length=200)
	message = models.TextField()

	def __str__(self):
		return self.name

	def absolute_url(self):
		return reverse('contact_detail', kwargs={'slug': self.slug, })

	def __unicode__(self):
		return self.name


class Tag(models.Model):
	tag_name = models.CharField(max_length=50, unique=True)
	created_at = models.DateTimeField(auto_now_add=True)


	def __str__(self):
		return self.tag_name


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
