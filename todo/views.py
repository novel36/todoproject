from datetime import datetime
from urllib import request
from django.forms import DateTimeField
from django.shortcuts import redirect, render

import todo
from todo.forms import TodoForm

from .models import Todo

# Create your views here.

# home view function
def home(request):
     todos={}
     todoform=TodoForm();
     if Todo.objects.count() > 0:
          todos=Todo.objects.all();
     context={
          'todos':todos,
          'todoform':todoform
     }
     return render(request,'index.html',context)


# function that add todo to database and redirect to home
def addtodo(request):
     
     if request.method == "POST":
          todo_added=Todo(body=request.POST['body'])
          todo_added.save()
          return redirect('home')
     else: 
          return redirect('home')
     # return redirect('home')

# function that check if todo is completed
def isCompleted(request):
     # checking if there is incoming request
     if request.method == 'GET':
          # Checking if the request is check request
          if 'todo' in request.GET:
               todo_id=request.GET['todo_id']
               todo_checked=Todo.objects.filter(id=todo_id).update(is_completed=True)
               return redirect('home')
          else:
          # Checking if the request is uncheck Request
               if 'uncheck_todo' in request.GET:
                    todo_id=request.GET['uncheck_todo']
                    todo_unchecked=Todo.objects.filter(id=todo_id).update(is_completed=False)
                    return redirect('home')
     else:
           return redirect('home')


# Delete ToDo From Database
def delete(request,id):
     if request.method == "GET":
          todo_id=id;
          todo_unchecked=Todo.objects.filter(id=todo_id).delete()
          return redirect('home')
     else:
          return redirect('home')