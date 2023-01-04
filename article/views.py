from article.models import Article
from article.serializers import ArticleReadingSerializer, ArticleCreationSerializer , ArticleUpdateSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

# 게시글 CRUD
class ArticleView(APIView):
    def get(self, request, **kwargs):
        if kwargs.get('article_id') is None:
            article_object = Article.objects.all()
            article_serializer = ArticleReadingSerializer(article_object, many=True)
            return Response(article_serializer.data, status=status.HTTP_200_OK)

        article_id = kwargs.get('article_id')
        article_object = Article.objects.get(article_id=article_id)
        article_serializer = ArticleReadingSerializer(article_object, many=False)
        return Response(article_serializer.data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        article_serializer = ArticleCreationSerializer(data = request.data, context={'request':request})
        if article_serializer.is_valid():
            article_serializer.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
# writer=self.request.user

        return Response(article_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, *args, **kwargs):
        if kwargs.get('article_id') is None:
            return Response('invalid request', status=status.HTTP_400_BAD_REQUEST)
        article_id = kwargs.get('article_id')
        article_object = Article.objects.get(id=article_id)
        article_serializer = ArticleUpdateSerializer(article_object, data = request.data)
        if article_serializer.is_valid():
            article_serializer.save()
            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        if kwargs.get('article_id') is None:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        article_object = Article.objects.get(article_id = kwargs.get('article_id'))
        article_object.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)