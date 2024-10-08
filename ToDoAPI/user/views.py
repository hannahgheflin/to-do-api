from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .models import *


# Create your views here.
def home(request):
    return render(request, "home.html")

def login(request):
    #get input
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        #check if username exists
        if not User.objects.filter(username=username).exists():
            messages.error(request, 'Username does not exists.')
            return redirect('/login/')
        
        #verify username and password are correct
        user = authenticate(username=username, password=password)
        
        #authentication failed
        if user is None:
            messages.error(request, "Password does not match.")
            return redirect('/login/')
        
        #authentication succes: redirects the user to home page
        else:
            login(request, user)
            return redirect('/home/')
    
    return render(request, 'login.html')

def register(request):
    #get input
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        #check if user already exiists
        user = User.objects.filter(username=username)
        
        #username already exists
        if user.exists():
            messages.info(request, "Username already exists.")
            return redirect('/register/')
        
        #otherwise, create account
        user = User.objects.create_user(
            first_name = first_name,
            last_name = last_name,
            username = username
        )
        
        #set user's password & save to database
        user.set_password(password)
        user.save()
        
        #redirect to login page
        return redirect('/login/')
    
    return render(request, 'register.html')