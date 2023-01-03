from rest_framework import serializers
from article.models import Article, Image

class ArticleImageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Image
        fields = ['image']
    
class ArticleSerializer(serializers.ModelSerializer):
    image = ArticleImageSerializer(many=True)
    class Meta:
        model = Article
        fields = ['writer' ,'content', 'image']

class ArticleUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        models = Article
        fields = ['content']
