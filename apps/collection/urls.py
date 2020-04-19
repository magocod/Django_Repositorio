"""
Rutas collection
"""

# Django
from django.urls import path

# local Django
from apps.collection.views import vcollection, vpcollection

urlpatterns = [
    path("collections/", vcollection.VCollectionList.as_view(), name="api_collections"),
    path(
        "collection/<int:pk>/",
        vcollection.VCollectionDetail.as_view(),
        name="api_collection_detail",
    ),
    path(
        "collection/relations/<int:pk>/",
        vcollection.VCollectionRelation.as_view(),
        name="api_collection_relation",
    ),
    # public
    path(
        "collections/slug_articles/",
        vpcollection.CollectionPublicListView.as_view(),
        name="api_collections_articles",
    ),
]
