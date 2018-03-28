# repositorioUNEFA
repositorio digital -> proyecto de pasantias UNEFA

-> Version 1.6 --> Proxima version + (Vuejs)

FRONT-END
#Bootstrap 4.0.0 -> https://getbootstrap.com/
#Materialize 0.100.2 -> http://archives.materializecss.com/0.100.2/

BACK-END
#Django 2.0.3 -> https://www.djangoproject.com/
#Django-rest-framework 3.7.7-> http://www.django-rest-framework.org/
#Sqlite3 3.22.0 --> https://www.sqlite.org/index.html
#Postgresql 10.3 --> https://www.postgresql.org/

Paquetes - Django
#django-cleanup==2.1.0
#django-unused-media==0.1.11
#django-debug-toolbar==1.9.1

Paquetes - Python
#factory-boy==2.10.0 

Javascript - Plugins
#Jquery 3.2.1
#Datatables 1.10.16
#Chosen 1.8.3

--> instrucciones

1) instalar entorno virtual python e instalar librerias con pip

pip install -r requirements.txt

2) Migrar la base de datos

python manage.py migrate

3) Crear Usuario

python manage.py createsuperuser (nombre/email/contraseña)

4) Ingresar data de prueba con fabricas de modelos 

python manage.py shell

//importar fabricas de modelos

from backend.fabricator.seeders import seederv2
s=seederv2

//ingresar cantidades (parametros numericos) -> backend/fabricator/seeders.py

s.seed_1(t,ti) t=temas, ti=tipos de items 
s.seed_2(t,i,cl,ct) t=tags, i=items, cl=colecciones, ct=categorias

5) Ejecutar servidor de desarrollo

python manage.py runserver

6) Ingresar a la direccion

http://localhost:8000
