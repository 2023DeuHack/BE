from article.models import Article
from article.serializers import ArticleReadingSerializer, ArticleCreationSerializer , ArticleUpdateSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User

# csrf
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

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
        # test user
        test_user = User.objects.get(pk=2)
        # save(test user -> request.user)
        if article_serializer.is_valid():
            article_serializer.save(writer_id=test_user)
            return Response(status=status.HTTP_204_NO_CONTENT)


        return Response(article_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, *args, **kwargs):
        if kwargs.get('article_id') is None:
            return Response('invalid request', status=status.HTTP_400_BAD_REQUEST)
        article_id = kwargs.get('article_id')
        article_object = Article.objects.get(article_id=article_id)
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

@api_view(['POST'])
@method_decorator(csrf_exempt, name='dispatch')
def article_like(request, article_id):
    if request.method == 'POST':
        article = get_object_or_404(Article, pk=article_id)
        # test_user
        test_user = User.objects.get(pk=2)
        # filter(test_user.pk -> request.user.pk)
        existed_user = article.article_likes.filter(pk=test_user.pk).exists()

        if existed_user:
            # 좋아요 상태 -> 좋아요 취소
            # remove(test_user -> request.user)
            article.article_likes.remove(test_user)
            return Response({'like' : 'unlike'} ,status=status.HTTP_200_OK)
        # 좋아요 아닌 상태 -> 좋아요
        # add(test_user -> request.user)
        article.article_likes.add(test_user)
        return Response({'like' : 'like'}, status=status.HTTP_200_OK)