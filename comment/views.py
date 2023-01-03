from django.shortcuts import render
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
from article.models import Article
from .serializer import CommentSerializer
from rest_framework import status
from rest_framework.response import Response

# Create your views here.
@api_view(['GET','POST'])
def comment_list_create(request,article_id):
    article = get_object_or_404(Article,pk=article_id)

    if request.method=="POST":
        serializer = CommentSerializer(data=request.data) #1
        if serializer.is_valid(raise_exception=True): #2
            serializer.save(article=article) 
        return Response(serializer.data,status=status.HTTP_201_CREATED)

    elif request.method=='GET':
        comments = article.comment_set.all()
        serializer=CommentSerializer(comments,many=True)
        return Response(serializer.data)