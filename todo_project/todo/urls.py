from django.urls import path

from . import views

urlpatterns = [
    path('', views.home_page, name= 'todo-home'),
    path('about', views.about_page, name= 'todo-about')
]