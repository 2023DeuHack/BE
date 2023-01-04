from rest_framework import serializers
from article.models import Article, Image

class ArticleImageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Image
        fields = ['image']
    
class ArticleSerializer(serializers.ModelSerializer):
    image = ArticleImageSerializer(many=True, read_only=True)

    class Meta:
        model = Article
        fields = ['content', 'image']

    def create(self, validated_data):
        article = Article.objects.create(**validated_data)
        image_data = self.context.get('request').FILES
        for image_data in image_data.getlist('image'):
            Image.objects.create(article=article, image=image_data)
        return article

class ArticleUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ['content']