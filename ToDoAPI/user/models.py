from django.db import models
from django.contrib.auth.models import User

# List class
class List(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

# List Item Class
class Task(models.Model):
    name = models.CharField(max_length=100)
    description = models.TestField(null=True, black=True)
    status = models.BooleanField()
    list = models.ForeignKey(List, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
