from django.db import models

class Todo(models.Model):
    name=models.fields.CharField(verbose_name="Todo name",max_length=100)

class Tasks(models.Model):
    name=models.fields.CharField(verbose_name="task name",max_length=100)

