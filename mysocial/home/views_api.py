from tkinter import N
from tkinter.messagebox import NO
from urllib import response
from .models import *
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.contrib import auth


class LoginView(APIView):

    def post(self,request):
        response={}
        response['status']=500
        response['message']='something went wrong'
        try:
            data = request.data
            if data.get('username') is None:
                response['message']='key user not found'
                raise Exception('key user not found')
            if data.get('password') is None:
                response['message']='key password not found'
                raise Exception('key password not found')

            check_user= User.objects.filter(username=data.get('username')).first()
        
            if check_user is None:
                response['message']='invalid username, user not found'
                raise Exception('invalid username, user not found')

            user_obj = authenticate(username= data.get('username'), password= data.get('password'))

            if user_obj:
                login(request,user_obj)
                response['status']=200
                response['message']='Welcome'
            else:
                response['message']='invalid password'
                raise Exception('invalid password')
        
        except Exception as e:
            print(e)

        return Response(response)



LoginView = LoginView.as_view()


class RegisterView(APIView):

    def post(self,request):
        response={}
        response['status']=500
        response['message']='something went wrong'
        try:
            data = request.data
            if data.get('username') is None:
                response['message']='key user not found'
                raise Exception('key user not found')
            if data.get('password') is None:
                response['message']='key password not found'
                raise Exception('key password not found')

            check_user= User.objects.filter(username=data.get('username')).first()
        
            if check_user:
                response['message']='username already exists'
                raise Exception('username already exists')
            user_obj= User.objects.create(username=data.get('username'))    
            user_obj.set_password(data.get('password'))
            user_obj.save()
            response['status']=200
            response['message']='user created'
        
        except Exception as e:
            print(e)

        return Response(response)

RegisterView=RegisterView.as_view()


class CommentView(APIView):
    def post(self,request):
        response={}
        response['status']=500
        response['message']='something went wrong'
        try:
            data = request.data
            if data.get('comment') is None:
                response['message']='comment not found'
                raise Exception('comment not found')
            myid=data.get('commented')
            myid=int(myid)
            post_obj=Postmodel.objects.get(id=myid)
            print(post_obj)
            comment_obj=comments.objects.create(commenter=request.user,commentedPost=post_obj, commentText=data.get('comment'))
            comment_obj.save()
            response['status']=200
            response['message']='commented'

        except Exception as e:
            print(e)

        return Response(response)
  

CommentView=CommentView.as_view()



class LikeView(APIView):
    def post(self,request):
        response={}
        response['status']=500
        response['message']='something went wrong'
        try:
            data = request.data
            myid=data.get('onpost')
            myid=int(myid)
            post_obj=Postmodel.objects.get(id=myid)
            if data.get('action')=='unlike':
                like_obj=likes.objects.get(likerUser=request.user,likedPost=post_obj)
                like_obj.delete()
            elif data.get('action')=='like':
                like_obj=likes.objects.create(likerUser=request.user,likedPost=post_obj)
                like_obj.save()
            response['status']=200
            response['message']='commented'
        except Exception as e:
            print(e)

        return Response(response)
  

LikeView=LikeView.as_view()



class FollowView(APIView):
    def post(self,request):
        response={}
        response['status']=500
        response['message']='something went wrong'
        try:
            data = request.data
            myid=data.get('person')
            myid=int(myid)
            if data.get('action')=='unfollow':
                follow_obj=Followmodel.objects.get(follower=request.user,following=myid)
                follow_obj.delete()
            elif data.get('action')=='follow':
                follow_obj=Followmodel.objects.create(follower=request.user,following=myid)
                follow_obj.save()
            response['status']=200
            response['message']='commented'
        except Exception as e:
            print(e)

        return Response(response)
  

FollowView=FollowView.as_view()