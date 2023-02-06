from rest_framework import serializers
from rest_framework.fields import SerializerMethodField

from webapp.models import Tag, Article, Comment


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ['id', 'title', 'content', 'author', 'tags', 'created_at', 'updated_at']
        read_only_fields = ['id', 'tags', 'created_at', 'updated_at']

class CommentSerializer(serializers.ModelSerializer):


    class Meta:
        model = Comment
        fields = ['id', 'text', 'article', 'author', 'created_at', 'updated_at']
        read_only_fields = ['id', 'article', 'author', 'created_at', 'updated_at']

        def get_author(self, obj):
            return obj.author.username


