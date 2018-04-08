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
from django.urls import path, include, re_path

#paquete herramientas de depuración
import debug_toolbar

#vistas django - login
from django.contrib.auth.views import login, logout_then_login

#reseteo de contraseña
from django.contrib.auth.views import password_reset, password_reset_done, password_reset_confirm, password_reset_complete

#vista inicial
from kernel.views import Indexv1

#vistas usuario
from backend.account.views import User_login, User_register

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

    #recuperacion de contraseña
    path('reset/password_reset', password_reset, 
        {'template_name':'account/password/reset_form.html',
        'email_template_name': 'account/password/reset_email.html'}, 
        name='password_reset'), 
    path('password_reset_done', password_reset_done, 
        {'template_name': 'account/password/reset_done.html'}, 
        name='password_reset_done'),
    re_path(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>.+)/$', password_reset_confirm, 
        {'template_name': 'account/password/reset_confirm.html'},
        name='password_reset_confirm'
        ),
    path(r'reset/done', password_reset_complete, {'template_name': 'account/password/reset_complete.html'},
        name='password_reset_complete'),

    #añadir directorios del storage
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
