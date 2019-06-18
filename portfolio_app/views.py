from django.shortcuts import render, redirect
from django.views.generic import *
from .models import *

# Create your views here.
def index(request):
	return render(request, 'index.html')

def blogs(request):
	return render(request, 'blogs.html')


def blog_detail(request):
	return render(request, 'blog_detail.html')

# def contact(request):
# 	return render(request, 'contactme.html')


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