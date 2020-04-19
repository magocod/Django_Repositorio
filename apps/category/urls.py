"""
Rutas category
"""

# Django
from django.urls import path

# local Django
from apps.category.views import vcategory, vpcategory

urlpatterns = [
    path("categories/", vcategory.VCategoryList.as_view(), name="api_categories"),
    path(
        "category/<int:pk>/",
        vcategory.VCategoryDetail.as_view(),
        name="api_category_detail",
    ),
    path(
        "categories/collections/",
        vpcategory.CategoryPublicListView.as_view(),
        name="api_categories_collections",
    ),
]
