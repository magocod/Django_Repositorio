"""
Rutas theme
"""

# Django
from django.urls import path

# local Django
from apps.theme.views import vtheme

urlpatterns = [
    path("themes/", vtheme.VThemeList.as_view(), name="api_themes"),
    path("theme/<int:pk>/", vtheme.VThemeDetail.as_view(), name="api_theme_detail",),
]
