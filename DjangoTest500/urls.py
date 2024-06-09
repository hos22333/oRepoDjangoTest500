"""
Definition of urls for DjangoWebProject1_Test1.
"""

from datetime import datetime
from django.urls import path
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from app import forms, views


urlpatterns = [
    path('', views.home, name='home'),
    path('WebPage01/', views.WebPage01, name='WebPage01'),
    path('WebPage02/', views.WebPage02, name='WebPage02'),
    path('WebPage03/', views.WebPage03, name='WebPage03'),
    path('WebPage04/', views.WebPage04, name='WebPage04'),
    path('WebPage05/', views.WebPage05, name='WebPage05'),
    path('WebPage06/', views.WebPage06, name='WebPage06'),
    path('WebPage07/', views.WebPage07, name='WebPage07'),
    path('WebPage08/', views.WebPage08, name='WebPage08'),
    path('WebPage09/', views.WebPage09, name='WebPage09'),


    path('oResuS/', views.oResuS, name='oResuS'),
    path('WebPage01/oResuS/', views.oResuS, name='oResuS'),    
    path('WebPage02/oResuB/', views.oResuB, name='oResuB'),      
    path('WebPage03/oResuG/', views.oResuG, name='oResuG'),       
    path('WebPage04/oResuP/', views.oResuP, name='oResuP'),        
    path('WebPage05/oResuT/', views.oResuT, name='oResuT'),    

    path("result", views.result, name="result"),
    path("form/result", views.result, name="result"),
    path('form/', views.form, name='form'),

    path('login/',
         LoginView.as_view
         (
             template_name='app/login.html',
             authentication_form=forms.BootstrapAuthenticationForm,
             extra_context=
             {
                 'title': 'Log in',
                 'year' : datetime.now().year,
             }
         ),
         name='login'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('admin/', admin.site.urls),
]
