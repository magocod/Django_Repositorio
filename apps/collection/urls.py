# Django
from django.urls import path

# local Django
from apps.collection.views import VCollection

urlpatterns = [
  path('collections/', VCollection.VCollectionList.as_view(), name='api_collections'),
  path('collection/<int:pk>/', VCollection.VCollectionDetail.as_view(), name='api_collection_detail'),
]