from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from . import views

app_name='blog'

urlpatterns = [
    path('',views.index,name='index'),
    path('<int:pageno>/',views.index,name='specificpage'),
    path('view/<int:postid>/',views.viewpost,name='viewpost'),
    path('create/',views.createpost,name='createpost'),
    path('newpost/',views.gotocreatepost),
    path('editpost/<int:postid>/',views.gotoeditpost),
    path('edit/<int:postid>/',views.editpost,name='editpost'),
    path('delete/<int:postid>',views.deletepost,name='deletepost'),
    path('createcomment/<int:postid>/',views.createcomment,name='comment')
]

