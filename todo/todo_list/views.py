from django.shortcuts import render,redirect
from django.http import HttpResponse
import json
from django.contrib.auth.models import User
from .models import todo_elements
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.urls import reverse
import urllib.parse
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

def index(request):
     return redirect("/login/")

def signup(request):
    if request.method=='POST':
        username=request.POST['Username']
        email=request.POST['Email']
        password1=request.POST['Password']
        password2=request.POST['Password1']
        user_exist=User.objects.filter(username=username)
        print(len(user_exist))
        if len(user_exist)>0:
            messages.error(request, 'This username has already been taken!')
            return redirect("/signup/")
        if password1!=password2:
            messages.error(request, 'Your password does not match!')
            return redirect("/signup/")
        user = User.objects.create_user(username,email ,password1)
        user.save()
        print(username)
        messages.success(request, 'Your account has been created!')
        return redirect("/login/")
    return render(request, "signup.html")

def signin(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['Password']
        user=authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('/todos/')
        else:
            messages.error(request,"Your credentials are invalid!")
            return redirect('/login/')
    return render(request, "login.html")

@csrf_exempt
def todos(request):
    if request.user.is_authenticated:
        username=request.user.username
        if request.method=='POST':
            todo_response = request.body.decode("utf-8")
            # print(todo_response)
            new_todo=todo_elements.objects.create(username=request.user,todo_title=todo_response)
            new_todo.save()
        if request.method=='DELETE':
            todo_response = request.body.decode("utf-8")
            todo_elements.objects.filter(username=request.user,todo_title=todo_response).delete()
        todos_object=todo_elements.objects.filter(username=request.user)
        todo_dict=[]
        for i in todos_object:
            todo_dict.append(i)
        return render(request, "todo.html",{'username':username,'todo_dict':todo_dict})
    return redirect("/login/")
    

def signout(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect('/login/')