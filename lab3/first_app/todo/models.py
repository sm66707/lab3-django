from operator import mod
from tabnanny import verbose
from tkinter import CASCADE
from django.db import models
from psycopg2 import Timestamp

class Todo(models.Model):
    name=models.fields.CharField(verbose_name="Todo name",max_length=100,unique=True)
    priority=models.fields.IntegerField(verbose_name="Todo priority",default=1)
    todo_date=models.fields.DateField(verbose_name="Date",default='2000-01-01')
    is_done=models.fields.BooleanField(default=False)
    notes=models.fields.TextField(default='')
    creation_time=models.DateTimeField(auto_now_add=True)
    update_time=models.DateTimeField(auto_now=True)

    def __str__(self) :
        return f"TOdo:{self.name} At Time {self.creation_time}"

    class Meta:
        verbose_name='Todo'
        verbose_name_plural='Todos'
        ordering=('-id',)


class Tasks(models.Model):
    name=models.fields.CharField(verbose_name="task name",max_length=100)
    todo=models.ForeignKey('todo',on_delete=models.CASCADE,null=True)

    def __str__(self):
        return f"Task{self.id} forTodo:{self.todo.name}"


# class Actor(models.Model):
#      pass


# class Movie(models.Model):
#     actors=models.ManyToManyField('actor')
#     director=models.ManyToManyField('director')
#     serial_number=models.OneToOneField('serial')

# class Director(models.Model):
#     user=models.ForeignKey('user')

# class serial(models.Model):
#     serial_key=models.CharField(max_length=50)