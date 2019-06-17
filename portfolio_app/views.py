from django.shortcuts import render
from django.views.generic import *

# Create your views here.
def index(request):
	return render(request, 'index.html')

def blogs(request):
	return render(request, 'blogs.html')


def blog_detail(request):
	return render(request, 'blog_detail.html')

# def contact(request):
# 	return render(request, 'contactme.html')


class Contact(View):

	def get(self, request, *args, **kwargs):
		return render(request, 'contactme.html')

	def post(self, request, *args, **kwargs):
		print(request.POST)
		name = request.POST.get('name')
		email = request.POST.get('email')
		subject = request.POST.get('subject')
		message = request.POST.get('message')
		return render(request, 'contactme.html')

def portfolio(request):
	return render(request, 'portfolio.html')

def services(request):
	return render(request, 'services.html')

def about(request):
	return render(request, 'aboutme.html')