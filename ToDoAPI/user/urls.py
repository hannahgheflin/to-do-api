from django.urls import path
from django.contrib import admin
from . import views

from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path("", views.home, name="home"),
    path("login/", views.login, name="login"),
    path("register/", views.register, name="register")
]