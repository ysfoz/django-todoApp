from django.shortcuts import get_object_or_404, redirect, render
from .models import Todo
from .forms import TodoForm, UpdateForm

def go_home(request):
    return render(request, 'todo/home.html')

def todo_list(request):
    todos = Todo.objects.all()
    context ={
        'todos':todos
    }

    return render(request,'todo/todo_list.html',context)

def add_todo(request):
    form = TodoForm()
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list')
    context = {
      'form' : form  
    }
    return render(request, 'todo/add_todo.html',context)

def update_todo(request,id):
    todo = get_object_or_404(Todo,id=id)
    form = UpdateForm(instance= todo)
    if request.method == 'POST':
        form = UpdateForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect('list')
     
    context = {
        'todo':todo,
         'form':form
     }   
    return render(request, 'todo/update_todo.html',context)

def delete_todo(request,id):
    todo = get_object_or_404(Todo,id=id)
    if request.method == 'POST':
        todo.delete()
        return redirect('list')
    context = {
        'todo':todo
    }
    return render(request, 'todo/delete_todo.html',context)
