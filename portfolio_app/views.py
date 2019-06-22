from django.shortcuts import render, redirect
from django.views.generic import *
from .models import *

# Create your views here.
def index(request):
	return render(request, 'index.html')


class BlogListView(ListView):
	model = Blog
	template_name = 'blogs.html'
	context_object_name = 'blogs'

	def get_context_data(self, **kwargs):
		context = super(BlogListView, self).get_context_data(**kwargs)
		context['latest'] = Blog.objects.filter().order_by('-created_at')[:5]
		context['categories'] = Category.objects.all()
		context['tags'] = Tag.objects.all()
		return context


class BlogDetailView(DetailView):
	model = Blog
	template_name = 'blog_detail.html'
	context_object_name = 'blog'

	def get_context_data(self, **kwargs):
		context = super(BlogDetailView, self).get_context_data(**kwargs)
		context['latest'] = Blog.objects.filter().order_by('-created_at')[:5]
		context['categories'] = Category.objects.all()
		context['tags'] = Tag.objects.all()
		obj = self.get_object()
		obj.blog_view_count += 1
		obj.save()
		return context


class ContactUs(View):

	def get(self, request, *args, **kwargs):
		return render(request, 'contactme.html')

	def post(self, request, *args, **kwargs):
		print(request.POST)
		name = request.POST.get('name')
		email = request.POST.get('email')
		subject = request.POST.get('subject')
		message = request.POST.get('message')
		Contact.objects.create(name=name,email=email,subject=subject,message=message)
		# return redirect({'success': 'Your messages is submitted'})
		return render(request, 'contactme.html', {'success': 'Your messages is submitted'})

class PortfolioListView(ListView):
	model = Portfolio
	template_name = 'portfolio.html'
	context_object_name = 'portfolios'


class ProjectListView(ListView):
	model = Project
	template_name = 'project.html'
	context_object_name = 'projects'

def services(request):
	return render(request, 'services.html')

def about(request):
	return render(request, 'aboutme.html')