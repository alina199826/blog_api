from django.http import JsonResponse, HttpResponseNotAllowed
from django.views import View
from django.shortcuts import get_object_or_404

import json

from rest_framework.views import APIView
from rest_framework.response import Response

from webapp.models import Article, Comment
from api_v2.serializers import ArticleSerializer, CommentSerializer

class ArticleView(APIView):
    def get(self, request, *args, **kwargs):
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = ArticleSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=400)

    def put(self, request, *args, **kwargs):
        article = get_object_or_404(Article, pk=kwargs.get('pk'))
        serializer = ArticleSerializer(data=request.data, instance=article)


        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=400)

    def delete(self, request, pk):
        article = get_object_or_404(Article.objects.all(), pk=pk)
        article.delete()
        return Response({
            "message": "Article with id `{}` has been deleted.".format(pk)
        }, status=204)

class ArticleDetailView(APIView):
    def get_object(self, pk):
        try:
            return Article.objects.get(pk=pk)
        except Article.DoesNotExist:
            raise 'error'

    def get(self, request, pk):
        article = self.get_object(pk)
        serializer = ArticleSerializer(article)
        return Response(serializer.data)
class CommentArticleView(APIView):

    def get(self, request, pk, *args, **kwargs):
        article = get_object_or_404(Article.objects.all(), pk=pk)
        if article is None:
            return Response({'error': 'Post not found'}, status=400)
        comments = Comment.objects.filter(pk=article)
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data, status=200)


