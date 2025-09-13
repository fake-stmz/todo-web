from django.db import models

# Create your models here.
class Task(models.Model): # Задания
    name = models.CharField(max_length=100) # Название задания
    description = models.TextField() # Описание задания
    status = models.CharField(max_length=50) # Статус
    creation_date = models.DateField(auto_now_add=True) # Дата создания
    deadline = models.DateField() # Дедлайн
    timespan = models.DurationField() # Время выполнения