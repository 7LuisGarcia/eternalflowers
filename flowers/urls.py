from django.urls import path
from . import views

app_name = 'flowers'

urlpatterns = [
    path('', views.home, name='home'),
    path('collections/', views.collections, name='collections'),
    path('services/', views.services, name='services'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('order/', views.order, name='order'),
]