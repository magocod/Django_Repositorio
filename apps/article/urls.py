# Django
from django.urls import path

# local Django
from apps.article.views import VArticle, VSpecification

urlpatterns = [
  path('articles/', VArticle.VArticleList.as_view(), name="api_articles"),
  path('article/<int:pk>/', VArticle.VArticleDetail.as_view(), name='api_article_detail'),
  path('article/relations/<int:pk>/', VArticle.VArticleRelation.as_view(), name='api_article_relation'),
  path(
    'articles/specification/',
    VSpecification.VSpecificationList.as_view(),
    name="api_specifications",
  ),
  path(
    'article/specification/<int:pk>/',
    VSpecification.VSpecificationDetail.as_view(),
    name='api_specification_detail',
  ),
]
