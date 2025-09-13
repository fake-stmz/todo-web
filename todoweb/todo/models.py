from django.db import models

# Create your models here.
class Task(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    status = models.CharField(max_length=50)
    creation_date = models.DateField(auto_now_add=True)
    deadline = models.DateField()
    timespan = models.DurationField()