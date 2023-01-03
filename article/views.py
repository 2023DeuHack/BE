from article.models import Article
from article.serializers import ArticleSerializer, ArticleUpdateSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import generics

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
        article_serializer = ArticleSerializer(data = request.data)
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

# 게시글 리스트.
# @api_view(['GET'])
# def articleList(request):
#     article = Article.objects.all()
#     serializer = ArticleSerializer(article, many=True)

#     return Response(serializer.data)

# # 게시글 생성.
# @api_view(['POST'])
# def articleCreate(request):
#     serializer = ArticleSerializer(data=request.data)

#     if serializer.is_valid():
#         serializer.save(writer=request.user)
    
#     article = Article.objects.all()
#     serializer = ArticleSerializer(article, many=True)

#     return Response(status=status.HTTP_204_NO_CONTENT)

# # 게시글 수정.
# @api_view(['PUT'])
# def articleUpdate(request, pk):
#     article = Article.objects.get(id=pk)
#     serializer = ArticleSerializer(instance=article, data=request.data)

#     if serializer.is_valid():
#         serializer.save()
    

#     article = Article.objects.all()
#     serializer = ArticleSerializer(article, many=True)

#     return Response(status=status.HTTP_204_NO_CONTENT)

# # 게시글 삭제
# @api_view(['DELETE'])
# def articleDelete(request, pk):
#     article = Article.objects.get(id=pk)

#     if article:
#         article.delete()

#     return Response(status=status.HTTP_204_NO_CONTENT)

# # 게시글 상세.
# @api_view(['GET'])
# def articleDetail(request, pk):
#     article = Article.objects.get(id=pk)
#     serializer = ArticleSerializer(article, many=False)

#     return Response(serializer.data)

# -----------------------------------------------------------
# class ArticleView(generics.ListCreateAPIView):
#     queryset = Article.objects.order_by('created_at').all()
#     serializer_class = ArticleSerializer

#     def list(self, request):
#         queryset = self.get_queryset()
#         serializer = ArticleSerializer(queryset, many=True)

#         return Response(serializer.data)

# class ArticleDetailView(generics.RetrieveUpdateDestroyAPIView):
#     serializer_class = ArticleSerializer

#     def get_object(self):
#         return Article.objects.get(id=self.kwargs['pk'])