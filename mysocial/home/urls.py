from django.urls import path
from .views import *


urlpatterns= [
    path('', home, name="home"),
    path('login/', login_view, name='login_view'),
    path('register', register_view, name='register_view'),
    path('logout/',logout_view,name='logout_view'),
    path('see-post/<slug>',see_post,name='see_post'),
    path('add-post/',add_post,name='add_post'),
    path('myposts/',myposts,name='myposts'),
    path('post_update/<slug>',post_update,name='post_update'),
    path('post_delete/<id>',post_delete,name='post_delete'),
    path('myaccount/',myaccount,name="myaccount"),
    path('people/',people,name="people"),
    path('visit/<id>',visit,name='visit'),
]