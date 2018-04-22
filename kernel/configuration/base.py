"""
Congiguracion global
"""

import os

#redirigir url
from django.urls import reverse_lazy

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
#SECRET_KEY = '+ds!f@wvyb^*w#d72jmukr1o1b4*t#t=^5s%$4!_5*l7od00_o'
with open('key.txt') as f:
    SECRET_KEY = f.read().strip()



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

# Internationalization
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


#despues de logear
LOGIN_REDIRECT_URL = reverse_lazy('account:dashboard')

#salir sesion
LOGOUT_REDIRECT_URL = reverse_lazy('login')
