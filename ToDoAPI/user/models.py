from django.db import models
from django.contrib.auth.models import User


# List Item Class
class Task(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    status = models.BooleanField()
    date_complete = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return self.name
    
    class meta:
        ordering = ['status']
