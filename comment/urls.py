from django.contrib import admin
from django.urls import path, include
from . import views
from rest_framework import routers


urlpatterns = [
    path('<int:article_id>/',views.CommentView.as_view()),
    path('<int:article_id>/<int:comment_id>/',views.CommentView.as_view()),

]