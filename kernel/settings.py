"""
Django settings for kernel project.

Generated by 'django-admin startproject' using Django 2.0.3.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import os
#redirigir url
from django.urls import reverse_lazy

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '+ds!f@wvyb^*w#d72jmukr1o1b4*t#t=^5s%$4!_5*l7od00_o'

#despues de logear
LOGIN_REDIRECT_URL = reverse_lazy('account:dashboard')

#salir sesion
LOGOUT_REDIRECT_URL = reverse_lazy('login')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

#Django Debug Toolbar - habilitar paneles
INTERNAL_IPS = ('127.0.0.1',)

# Application definition

INSTALLED_APPS = [
	#django
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    #paquetes
    'debug_toolbar',
    'rest_framework',
    'django_cleanup',
    'django_unused_media',
    'django_filters',
    #aplicaciones --> backend
    'backend.account',
    'backend.api',
    'backend.fabricator',
    'backend.grabber',
    'backend.seeker',
    'backend.storage',
]


# Seguridad (perfiles, permisos, autenticacion)
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    #debug-toolbar
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

# rutas globales
ROOT_URLCONF = 'kernel.urls'

# Motor de plantillas django
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        #directorio plantillas html
        'DIRS': [os.path.join(BASE_DIR,'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

#configuracion web
WSGI_APPLICATION = 'kernel.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    #configuracion por defecto
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }

    #'default': {#Postgresql
    #    'ENGINE': 'django.db.backends.postgresql_psycopg2',
    #    'NAME': 'repv1',
    #    'USER':'postgres',
    #    'PASSWORD':'24682468',
    #    'HOST':'localhost',
    #    'PORT':5432,
    #}

}


# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

#ruta estilos --> aplicacion
STATIC_URL = '/static/'

#ruta base directorio de estilos --> servidor /ejemplo/static
STATIC_ROOT = 'staticfiles'

#directorio de estilos /archivos estaticos
STATICFILES_DIRS = (
    os.path.join(BASE_DIR,'static'),
)

#ruta archivos --> aplicacion
MEDIA_URL = '/media/'

#ruta base directorio de archivos --> servidor /media
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')


#api renderizar
REST_FRAMEWORK = {

   'DEFAULT_PERMISSION_CLASSES': (
   'rest_framework.permissions.AllowAny',
    ),

    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',

    ),
    'DEFAULT_PAGINATION_CLASS': 
        'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 100

}

#email mailtrap
#EMAIL_USE_TLS = False
EMAIL_HOST = 'smtp.mailtrap.io'
EMAIL_HOST_USER = 'fb49918a61595b'
EMAIL_HOST_PASSWORD = 'f41911cfabfaa7'
EMAIL_PORT = '2525'
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'