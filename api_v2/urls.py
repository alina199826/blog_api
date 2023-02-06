from django.urls import path, include
from api_v2.views import ArticleView, CommentArticleView, ArticleDetailView

app_name = 'api_v2'

article_url = [
    path('', ArticleView.as_view()),
    path('<int:pk>/', ArticleDetailView.as_view()),
    path('comment', CommentArticleView.as_view()),
    path('comment/<int:pk>/', CommentArticleView.as_view())
]

comment_url = [

    path('', CommentArticleView.as_view()),
    path('<int:pk>/', CommentArticleView.as_view())
]

urlpatterns = [
    path('article/', include(article_url)),
    path('comment/', include(comment_url))
]