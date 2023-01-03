from django.contrib.auth.models import User
from django.db import models
from django.contrib import admin

# 게시물
class Article(models.Model):
    writer = models.ForeignKey(User,related_name='article' , on_delete=models.CASCADE, null=False)
    content = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=False)
    location = models.CharField(max_length=30, null=True)

    class Meta:
        db_table = 'article'

# 게시물 이미지
class Image(models.Model):
    image = models.ImageField(upload_to='article', null=False)
    article = models.ForeignKey(Article,related_name='image' ,on_delete=models.CASCADE)

    class Meta:
        db_table = 'image'