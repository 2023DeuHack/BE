from rest_framework import serializers
from article.models import Article, Image
from comment.serializer import CommentReadingSerializer

class ArticleImageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Image
        fields = ['image']

# GET
class ArticleReadingSerializer(serializers.ModelSerializer):
    image = ArticleImageSerializer(many=True, read_only=True)

    class Meta:
        model = Article
        fields = ['article_id', 'writer','content', 'image', 'location']

# POST
class ArticleCreationSerializer(serializers.ModelSerializer):
    image = ArticleImageSerializer(many=True, read_only=True)

    class Meta:
        model = Article
        fields = ['content', 'image', 'location']

    def create(self, validated_data):
        article = Article.objects.create(**validated_data)
        image_data = self.context.get('request').FILES
        for image_data in image_data.getlist('image'):
            Image.objects.create(article=article, image=image_data)
        return article

# PUT
class ArticleUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ['content', 'location']