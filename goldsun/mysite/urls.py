from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home, name='index'),
    path('index.html', views.Home, name='index'),
    path('about.html', views.About, name='about'),
    path('contact.html', views.Contact, name='contact'),
    path('faq.html', views.Faq, name='faq'),



]
