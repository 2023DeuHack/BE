from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    # path('list/', views.articleList, name='list'),
    # path('create/', views.articleCreate, name='create'),
    # path('update/<int:pk>', views.articleUpdate, name='update'),
    # path('delete/<int:pk>/', views.articleDelete, name='delete'),
    # path('detail/<int:pk>/', views.articleDetail, name='detail'),
    path('', views.ArticleView.as_view()),
    path('<int:article_id>/', views.ArticleView.as_view()),
    # path('article/<int:pk>', views.ArticleDetailView.as_view(), name='articledetail'),
]
 