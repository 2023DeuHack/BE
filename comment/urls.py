from django.contrib import admin
from django.urls import path, include
from . import views
from rest_framework import routers


urlpatterns = [
    # 댓글 생성, 조회
    path('<int:article_id>/',views.CommentView.as_view()),
    # 대댓글 생성, 조회, 댓글 삭제, 대댓글 삭제
    path('<int:article_id>/<int:comment_id>/',views.CommentView.as_view()),
]