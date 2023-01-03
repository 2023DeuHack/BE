from django.db import models
from django.contrib.auth.models import User
from article.models import Article

class Comment(models.Model):
    content = models.CharField(max_length=200, null=False)
    parent_id = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)
    writer = models.ForeignKey(User, null=False)
    article_id = models.ForeignKey(Article, null=False)
    created_at = models.DateTimeField(auto_now_add=True, null=False)

    class Meta:
        db_table = 'comment'