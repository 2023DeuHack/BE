from django.shortcuts import render
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
from article.models import Article
from .serializer import CommentReadingSerializer, CommentCreationSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Comment

class CommentView(APIView):
    def get(self, request, **kwargs):
        if kwargs.get('comment_id') is None:
            article_id = kwargs.get('article_id')
            comment_object = Comment.objects.filter(article_id=article_id, parent_id=None)
            comment_serializer = CommentReadingSerializer(comment_object, many=True)
            return Response(comment_serializer.data, status=status.HTTP_200_OK)

        parent_id = kwargs.get('comment_id')
        comment_object = Comment.objects.filter(parent_id=parent_id)
        comment_serializer = CommentReadingSerializer(comment_object, many=True)
        return Response(comment_serializer.data, status=status.HTTP_200_OK)

    def post(self, request, **kwargs):
        if kwargs.get('comment_id') is None:
            article_id=kwargs.get('article_id')
            article = Article.objects.get(article_id=article_id)
            comment_serializer = CommentCreationSerializer(data=request.data)
            if comment_serializer.is_valid():
                comment_serializer.save(article_id=article)
            # , writer=request.user
                return Response(status=status.HTTP_201_CREATED)

        article_id=kwargs.get('article_id')
        parent_id=kwargs.get('comment_id')
        article = Article.objects.get(article_id=article_id)
        parent_comment = Comment.objects.get(comment_id=parent_id)
        comment_serializer = CommentCreationSerializer(data=request.data)
        if comment_serializer.is_valid():
            comment_serializer.save(article_id=article, parent_id=parent_comment)
            # , writer=request.user
            return Response(status=status.HTTP_201_CREATED)

    def delete(self, request, **kwargs):
        if kwargs.get('comment_id') is None:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        comment_id = kwargs.get('comment_id')
        comment_object = Comment.objects.get(comment_id=comment_id)
        comment_object.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)