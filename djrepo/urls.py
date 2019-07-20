"""djrepo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

# urls api
from apps.category.urls import urlpatterns as apicategory
from apps.collection.urls import urlpatterns as apicollection
from apps.tag.urls import urlpatterns as apitag
from apps.theme.urls import urlpatterns as apitheme
from apps.user.urls import urlpatterns as apiuser

# concatenar rutas
apiurls = apicategory + apicollection + apitheme + apitag + apiuser

urlpatterns = [
	# web
  path('admin/', admin.site.urls),
  # api
  path('api/', include(apiurls)),
]
