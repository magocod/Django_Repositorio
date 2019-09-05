# Django
from django.urls import path

# local Django
from apps.collection.views import VCollection, VPCollection

urlpatterns = [
  path('collections/', VCollection.VCollectionList.as_view(), name='api_collections'),
  path('collection/<int:pk>/', VCollection.VCollectionDetail.as_view(), name='api_collection_detail'),
  path('collection/relations/<int:pk>/', VCollection.VCollectionRelation.as_view(), name='api_collection_relation'),
  # public
  path('collections/slug_articles/', VPCollection.VCollectionSlugList.as_view(), name='api_collections_articles'),
]