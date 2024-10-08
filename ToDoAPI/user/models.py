from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    tasks = []
    
class Task(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    status = models.BooleanField()