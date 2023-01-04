from django.urls import path
from . import views

urlpatterns = [
    path('', views.ArticleView.as_view()),
    path('<int:article_id>', views.ArticleView.as_view()),
]