from django.urls import path, include
from . import views

app_name = 'portfolio'

urlpatterns = [
    path('', views.index, name='index'),
    path('blogs/', views.BlogListView.as_view(), name='blogs'),
    path('blog_detail/<int:pk>', views.BlogDetailView.as_view(), name='blog_detail'),
    # path('contact/', views.contact, name='contact'),
    path('contact/', views.ContactUs.as_view(), name='contact'),
    path('portfolio/', views.PortfolioListView.as_view() , name='portfolio'),
    path('project/', views.ProjectListView.as_view(), name='project'),
    path('services/', views.services, name='services'),
    path('about/', views.about, name='about'),
]