from django.contrib import admin
from django.urls import path, include
from .import views

urlpatterns = [
    path('', views.index, name="index"),
    path('search/', views.search, name="search"),
    path('about/', views.about, name="about"),
    path('contact/', views.contact_us, name="contact"),
    path('contact_save/', views.contact_save, name="contact_save"),
]
