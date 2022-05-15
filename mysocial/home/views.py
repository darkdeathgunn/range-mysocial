from imp import reload
from multiprocessing import context
from optparse import IndentedHelpFormatter
from django.shortcuts import render,redirect
from django.core.files.storage import FileSystemStorage
from django.contrib import auth
import os
from .form import *


def home(request):
    data=likeCounter(request)
    posts=data["posts"]
    context = {"posts":posts}
    return render(request,'home.html',context)
#####################################


def login_view(request):
    return render(request,'login.html')
################################


def register_view(request):
    return render(request, 'register.html')
##################################################


def logout_view(request):
    auth.logout(request)
    return redirect('/')
##################################################


def see_post(request,slug):
    context={}
    try:
        post_obj=Postmodel.objects.filter(slug=slug).first()
        num=likes.objects.filter(likedPost=post_obj.id).count()
        post_obj.likeCount=num
        context['post']=post_obj
        context['likeObj']=likes.objects.filter(likedPost=post_obj.id,likerUser=request.user)
        val=False
        for like in context['likeObj']:
            val=like.getstate()
        context['like']=val
        context['comments']=comments.objects.filter(commentedPost_id=post_obj.id)
    except Exception as e:
        print(e)
    return render(request,'see_post.html',context)
##################################################


def add_post(request):
    context={}
    try:
        if request.method=='POST':
            title=request.POST.get('title')
            user=request.user
            content=request.POST.get('content')

            post_obj=Postmodel.objects.create(user=user,title=title,content=content)
            print(post_obj)
            return reload('/add_post/')
    except Exception as e:
        print(e)
    return render(request,'add_post.html',context)
##################################################


def myposts(request):
    context={}
    try:
        post_objs=Postmodel.objects.filter(user=request.user)
        context['post_objs']=post_objs
    except Exception as e:
        print(e)
    return render(request,'myposts.html',context)
##################################################


def post_update(request,slug):
    context={}
    try:
        post_obj=Postmodel.objects.get(slug=slug)
        if post_obj.user != request.user:
            return redirect('/')
        if request.method=='POST':
            title=request.POST.get('title')
            content=request.POST.get('content')
            post_obj.title=title
            post_obj.content=content
            post_obj.save()
        context['post_obj']=post_obj
    except Exception as e:
        print(e)
    return render(request, 'post_update.html',context)
##################################################


def post_delete(request,id):
    try:
        post_obj=Postmodel.objects.get(id=id)
        if post_obj.user == request.user:
            post_obj.delete()
    except Exception as e:
        print(e)
    return redirect('/myposts/')
##################################################


def myaccount(request):
    context={}
    myid=request.user.id
    context['follower']=Followmodel.objects.filter(following=myid).count()
    context['following']=Followmodel.objects.filter(follower=request.user).count()
    return render(request,'myaccount.html',context)
##################################################


def people(request):
    context={}
    try:
        user_Objs=User.objects.all().exclude(id=request.user.id)
        context['user_Objs']=user_Objs
    except Exception as e:
        print(e)
    return render(request,'people.html',context)
#####################################################


def visit(request,id):
    context={}
    try:
        cuser=User.objects.get(id=id)
        myid=cuser.id
        context['follower']=Followmodel.objects.filter(following=myid).count()
        context['following']=Followmodel.objects.filter(follower=cuser).count()
        context['cuser']=cuser
        context['followObj']=Followmodel.objects.filter(follower=request.user,following=cuser.id)
        val=False
        for follow in context['followObj']:
            val=follow.getstate()
        context['follow']=val

    except Exception as e:
        print(e)
    return render(request, 'visit.html',context)
##################################################