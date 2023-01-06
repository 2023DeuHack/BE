from django.contrib.auth.models import User
from django.db import models

# 게시물
class Article(models.Model):
    article_id = models.AutoField(primary_key=True, serialize=False)
    writer_id = models.ForeignKey(User,related_name='article' , on_delete=models.CASCADE, null=False)
    content = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=False)
    location = models.CharField(max_length=30, null=True)
    article_likes = models.ManyToManyField(User,related_name='article_like')

    class Meta:
        db_table = 'article'

# 게시물 이미지
class Image(models.Model):
    image = models.ImageField(upload_to='article', null=False)
    article_id = models.ForeignKey(Article,related_name='image' ,on_delete=models.CASCADE, null=False)

    class Meta:
        db_table = 'image'