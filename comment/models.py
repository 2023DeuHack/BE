from django.db import models
from django.contrib.auth.models import User
from article.models import Article

class Comment(models.Model):
    content = models.CharField(max_length=200, null=False)
    parent_id = models.IntegerField(null=True)
    writer = models.ForeignKey(User, null=False)
    article_id = models.ForeignKey(Article)

    class Meta:
        db_table = 'comment'