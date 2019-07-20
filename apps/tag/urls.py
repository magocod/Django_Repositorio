# Django
from django.urls import path

# local Django
from apps.tag.views import VTag

urlpatterns = [
  path('tags/', VTag.VTagList.as_view(), name='api_tags'),
  path('tag/<int:pk>/', VTag.VTagDetail.as_view(), name='api_tag_detail'),
]