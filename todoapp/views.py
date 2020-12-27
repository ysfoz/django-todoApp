from django.shortcuts import render
from .models import Todo

def home(request):
    return render(request, 'todo/home.html')

def todo_list(request):
    todos = Todo.objects.all()
    context ={
        'todos':todos
    }

    return render(request,'todo/todo_list.html',context)

def add_todo(request):
    pass
