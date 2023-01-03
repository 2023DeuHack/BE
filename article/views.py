from article.models import Article
from article.serializers import ArticleSerializer, ArticleUpdateSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import viewsets

# 게시글 CRUD
class ArticleView(APIView):
    def get(self, request, **kwargs):
        if kwargs.get('article_id') is None:
            article_query = Article.objects.all()
            article_serializer = ArticleSerializer(article_query, many=True)
            return Response(article_serializer.data, status=status.HTTP_200_OK)

        article_id = kwargs.get('article_id')
        article_serializer = ArticleSerializer(Article.objects.get(id=article_id))
        return Response(article_serializer.data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        article_serializer = ArticleSerializer(data = request.data, context={'request':request})
        if article_serializer.is_valid():
            article_serializer.save(writer=self.request.user)
            return Response(status=status.HTTP_204_NO_CONTENT)

        return Response(article_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, *args, **kwargs):
        if kwargs.get('article_id') is None:
            return Response('invalid request', status=status.HTTP_400_BAD_REQUEST)
        article_id = kwargs.get('article_id')
        article_object = Article.objects.get(id=article_id)
        article_serializer = ArticleUpdateSerializer(article_object, data = request.data)
        if article_serializer.is_valid:
            article_serializer.save()
            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        if kwargs.get('article_id') is None:
            return Response('invalid request', status=status.HTTP_400_BAD_REQUEST)
        article_object = Article.objects.get(id = kwargs.get('article_id'))
        article_object.delete()
        return Response('delete', status=status.HTTP_200_OK)