"""
Rutas Tag
"""

# Django
from django.urls import path

# local Django
from apps.tag.views import vtag

urlpatterns = [
    path("tags/", vtag.VTagList.as_view(), name="api_tags"),
    path("tag/<int:pk>/", vtag.VTagDetail.as_view(), name="api_tag_detail"),
]
