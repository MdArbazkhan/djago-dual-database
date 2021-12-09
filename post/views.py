from django.shortcuts import render, redirect
from django.http.response import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from datetime import datetime

import post
from .models import Post
import random

# Create your views here.
def login_user(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            return redirect('/landing')
        else:
            return render(request, 'post/login.html')
    else:
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/landing')
        else:
            return render(request, 'post/login.html')
            
            

@login_required
def landingpage(request):
    return render(request, 'post/landing-page.html')


def logout_user(request):
    logout(request)
    return redirect('login-page')
    

def generate_post_id():
    final_post_id = ''
    characters_str = 'abcdefghijklmnopqrstuvwxyz0123456789'
    for x in range(10):
        final_post_id += random.choice(characters_str)
        
    return final_post_id

def addNewPost(request):
    if request.method == 'GET':
        return render(request,'post/add-new.html')
    else:
        new_text = request.POST['textarea']
        post_id = generate_post_id()
        new_post = Post(user=request.user, post_id=post_id, text=new_text)
        new_post.save()
        return redirect('list')

def list(request):
    post_object = Post.objects.filter(user=request.user)
    return render(request, 'post/list.html',{
        'post_object':post_object
    })


def edit(request,post_id):
    if request.method == 'GET':
        post_obj = Post.objects.get(post_id=post_id)
        return render(request, 'post/edit.html',{
            'post_obj':post_obj
        })
    else:
        new_text = request.POST['textarea']
        post_obj = Post.objects.get(post_id=post_id)
        post_obj.updated_at = datetime.now()
        post_obj.text = new_text
        post_obj.save()
        return redirect('list')
