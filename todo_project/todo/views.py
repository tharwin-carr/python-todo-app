from django.shortcuts import render

todos = [
    {'title': 'Clean the car', 'complete': False},
    {'title': 'Pickup kids from school', 'complete': True}
]

def home_page(request):
    context = {
        'todos': todos
    }
    return render(request, 'todo/home.html', context)

def about_page(request):
    return render(request, 'todo/about.html')
