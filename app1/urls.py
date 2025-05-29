from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('gallery/', views.gallery, name='gallery'),
    path('properties/', views.properties, name='properties'),
    path('contact/', views.contact_view, name='contact'),
    path('rooms/', views.rooms_view, name='rooms'),
    path('book/', views.book, name='book'),
    path('contact/', views.contact_view, name='contact'),
    path('thank-you/', views.thank_you_view, name='thank_you'),
   path('about/', views.about, name='about'),
     
   

]


