from django.db import models
from rest_framework import serializers
from .models import Comment

# GET
class CommentReadingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['comment_id', 'writer','content','created_at']

# POST
class CommentCreationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['content']

# GET: writer, content, created_at
# POST: content