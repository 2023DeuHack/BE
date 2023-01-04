from django.db import models
from django.contrib.auth.models import User
from article.models import Article

class Comment(models.Model):
    comment_id = models.AutoField(primary_key=True)
    content = models.CharField(max_length=200, null=False)
    parent_id = models.IntegerField(null=True)
    writer = models.ForeignKey(User,on_delete=models.SET_NULL ,null=True)
    article = models.ForeignKey(Article,on_delete=models.SET_NULL ,null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=False)

    class Meta:
        db_table = 'comment'