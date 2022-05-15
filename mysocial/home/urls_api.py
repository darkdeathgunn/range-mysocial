from django.urls import path
from .views_api import *


urlpatterns= [
    path('login/',LoginView),
    path('register/',RegisterView),
    path('comment/',CommentView),
    path('like/',LikeView),
    path('follow/',FollowView),
]