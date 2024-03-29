from django.urls import path, include
from api_v2.views import ArticleView, ArticleDetailView

app_name = 'api_v2'

article_url = [
    path('', ArticleView.as_view()),
    path('<int:pk>/', ArticleDetailView.as_view()),

]


urlpatterns = [
    path('article/', include(article_url)),

]