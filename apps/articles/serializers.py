from rest_framework import serializers
from django.db import models


from .models import Article

class ArticleListSerializer(serializers.ListSerializer):
    def get_image_url(self, image):
        request = self.context['request']
        a = request.build_absolute_uri(image.url)
        return a

    def to_representation(self, data):
        iterable = data.all() if isinstance(data, models.Manager) else data
        return [{
            'slug': item.slug,
            'title': item.title,
            'user': item.user.username,
            'image_url': self.get_image_url(item.image) if item.image else None,
        } for item in iterable]


class ArticleSerializer(serializers.ModelSerializer):
    # user = serializers.SerializerMethodField(method_name='get_username')

    class Meta:
        model = Article
        read_only_fields = ['user', 'slug']
        list_serializer_class = ArticleListSerializer


    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)
    
    # def get_username(self, obj):
    #     return obj.user.username
    


