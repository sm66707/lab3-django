from logging import warning
from multiprocessing import Condition, context
from django.shortcuts import render,HttpResponse,redirect,reverse
from django.http.response import JsonResponse
from pprint import pprint
from .models import Todo,Tasks

# Create your views here.
# my_todos = {
#     'one': {'name':'python', 'priority':'1','is_done':False, 'description':"this is desc"},
#     'two': {'name':'django', 'priority':'2','is_done':False,'description':"this is desc"},
#     'three': {'name':'node', 'priority':'3','is_done':False,'description':"this is desc"}
# }

# def todo_json_home(request):
#     return JsonResponse(my_todos)

# def todo_home(request,**kwargs):
#     print(kwargs)
#     target_todo_name=kwargs.get('todo_name')
#     print("Todo Name: " , target_todo_name)
#     todo_details= my_todos.get(target_todo_name)
#     return HttpResponse(f"hello from {todo_details} ")
  
def todo_list(request,**kwargs):
   
    return render(request,'todo/todo.html',context={'my_todos':my_todos})

def todo_details(request,**kwargs):
    target_todo_name=kwargs.get('todo_name')
    todo_details= my_todos.get(target_todo_name)
    return render(request,'todo/todo_detail.html',context={'my_todo':todo_details})

def todo_delete(request,**kwargs):
    target_todo_name=kwargs.get('todo_name')
    my_target_todo=my_todos.get(target_todo_name)

    if  my_target_todo.get('is_done'):
         my_todos.pop(target_todo_name)

    else:
        return render(request ,'todo/todo.html',context={'my_todos':my_todos,'warning_msg':"cannot delete unfinished tasks"})

    return redirect(reverse('todo:list'))

def todo_done(request,**kwargs):
    task_name=kwargs.get('todo_name')
    my_target_todo=my_todos.get(task_name)
    my_target_todo['is_done']=True
    return redirect(reverse('todo:list'))

def todo_edit(request,**kwargs):
    target_todo_name=kwargs.get('todo_name')
    # todo_details= my_todos.get(target_todo_name)
    return render(request,'todo/todo_edit.html',context={'my_todo':target_todo_name})

def todo_update(request,**kwargs):
    task_name=kwargs.get('todo_name')
    my_target_todo=my_todos.get(task_name)
    my_target_todo['is_done']=True
    my_target_todo['name']='noname'
    return redirect(reverse('todo:list'))