#configuracion para desarrollo

# global
from kernel.base import *


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

#Django Debug Toolbar - habilitar paneles
INTERNAL_IPS = ('127.0.0.1',)

# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    #configuracion por defecto
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }

    #Postgresql
    #'default': {
    #    'ENGINE': 'django.db.backends.postgresql_psycopg2',
    #    'NAME': 'repv1',
    #    'USER':'postgres',
    #    'PASSWORD':'24682468',
    #    'HOST':'localhost',
    #    'PORT':5432,
    #}

}


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

#ruta estilos --> aplicacion
STATIC_URL = '/static/'

#ruta base directorio de estilos --> servidor /ejemplo/static
STATIC_ROOT = 'staticfiles'

#directorio de estilos /archivos estaticos desarrollo
STATICFILES_DIRS = (
    os.path.join(BASE_DIR,'static'),
)

#ruta archivos --> aplicacion
MEDIA_URL = '/media/'

#ruta base directorio de archivos --> servidor /media
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')
