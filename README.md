## RepositorioUNEFA

> Repositorio digital, proyecto de pasantias UNEFA

## FRONT-END

* Bootstrap 4.0.0 -> https://getbootstrap.com/
* Materialize 0.100.2 -> http://archives.materializecss.com/0.100.2/

```bash
Proxima version Vuejs -> https://github.com/magocod/Vue_repositorio
```

## BACK-END

* Django 2.0.3 -> https://www.djangoproject.com/
* Django-rest-framework 3.7.7-> http://www.django-rest-framework.org/
* Sqlite3 3.22.0 --> https://www.sqlite.org/index.html
* Postgresql 10.3 --> https://www.postgresql.org/

## Paquetes - Django

* django-cleanup==2.1.0
* django-unused-media==0.1.11
* django-debug-toolbar==1.9.1

## Paquetes - Python

* factory-boy==2.10.0 

## Javascript - Plugins

* Jquery 3.2.1
* Datatables 1.10.16
* Chosen 1.8.3

## Directorios Estructura
-------------------

      backend/             Procesamiento de informacion
             /account/     Control de usuarios,perfiles,permisos
             /api/         Intercambiar informacion JSON,XML
             /fabricator/  Ingresar data de prueba
             /grabber/     Formularios para ingresar data
             /seeker/      Busquedas y filtrado
             /storage/     Modelos y logica de negocio
      kernel/              Configuracion general
      static/              Archivos estaticos
      templates/           Codigo Html
     
## instrucciones

instalar entorno virtual python e instalar librerias con pip

```bash
pip install -r requirements.txt
```

Migrar la base de datos

```bash
python manage.py migrate
```

Crear Usuario

```bash
python manage.py createsuperuser (nombre/email/contraseña)
```

Ingresar data de prueba con fabricas de modelos 

```bash
python manage.py shell
```

importar fabricas de modelos

```bash
from backend.fabricator.seeders import seederv2
s=seederv2
```

ingresar cantidades (parametros numericos) -> backend/fabricator/seeders.py

```bash
s.seed_1(t,ti) t=temas, ti=tipos de items 
s.seed_2(t,i,cl,ct) t=tags, i=items, cl=colecciones, ct=categorias
```

Ejecutar servidor de desarrollo

```bash
python manage.py runserver
```

Ingresar a la direccion

```bash
http://localhost:8000
```

