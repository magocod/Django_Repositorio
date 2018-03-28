"""kernel URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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

#añadir carpeta
from django.conf import settings
from django.conf.urls.static import static

#manejo de rutas
from django.urls import path, include

#paquete herramientas de depuración
import debug_toolbar

#vistas django - login
from django.contrib.auth.views import login, logout_then_login

#vista inicial
from kernel.views import Indexv1

#vistas usuario
from backend.account.views import User_login, User_register, User_password

urlpatterns = [

    #paquetes
	#debug-toolbar
	path('__debug__/', include(debug_toolbar.urls)),

    #api-rest
    path('api-auth/', include('rest_framework.urls'),name='api_rest'),

	#administrador django (default)
    path('admin/', admin.site.urls),

    #vista principal
    path('', Indexv1.as_view(),name='index'),

    #componentes --> apps --> backend
    path('account/', include('backend.account.urls')),
    path('api/', include('backend.api.urls')),
    path('grabber/', include('backend.grabber.urls')),
    path('seeker/', include('backend.seeker.urls')),

    #autenticacion
    path('accounts/login/', login, {'template_name':'account/authenticate/login.html'}, name='login'),
    #path('accounts/login/', User_login.as_view(), name='login'),
    #salir
    path('logout', logout_then_login, name='logout'),
    #registrar fuera del admin
    path('register', User_register.as_view(), name='user_register'),
    #recuperar contraseña
    path('password', User_password.as_view(), name='user_password'),

    #añadir directorios del storage
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
