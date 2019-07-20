# Django
from django.urls import path

# local Django
from apps.theme.views import VTheme

urlpatterns = [
  path('themes/', VTheme.VThemeList.as_view(), name='api_themes'),
  path('theme/<int:pk>/', VTheme.VThemeDetail.as_view(), name='api_theme_detail'),
]