from django.contrib import admin
from user.models import *
from .models import User

admin.site.register(User)
admin.site.register(Task)
admin.site.register(List)
