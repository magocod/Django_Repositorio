# Django
from django.urls import path

# local Django
from apps.category.views import VCategory, VPCategory

urlpatterns = [
  path('categories/', VCategory.VCategoryList.as_view(), name="api_categories"),
  path('category/<int:pk>/', VCategory.VCategoryDetail.as_view(), name='api_category_detail'),
  path('categories/collections/', VPCategory.VCategorySlugList.as_view(), name='api_categories_collections'),
]