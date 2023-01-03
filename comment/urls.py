from django.contrib import admin
from django.urls import path, include
from . import views
from rest_framework import routers


urlpatterns = [
    path('',views.article_list_create,name='article_list_create'), #GET POST
    path('<int:article_id>/',views.article_detail_update_delete,name='article_detail_update_delete'),
    path('<int:article_id>/comments/',views.comment_list_create,name='comment_list_create'),
    path('<int:article_id>/comments/<int:comment_id>/',views.comment_detail_update_delete,name='comment_detail_update_delete'),
]