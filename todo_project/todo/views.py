from django.shortcuts import render

from .models import SingleTodo


def home_page(request):
    context = {
        'todos': SingleTodo.objects.all()
    }
    return render(request, 'todo/home.html', context)

def about_page(request):
    return render(request, 'todo/about.html')
