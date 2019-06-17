from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('blogs/', views.blogs, name='blogs'),
    path('blog_detail/', views.blog_detail, name='blog_detail'),
    # path('contact/', views.contact, name='contact'),
    path('contact/', views.Contact.as_view(), name='contact'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('services/', views.services, name='services'),
    path('about/', views.about, name='about'),
]