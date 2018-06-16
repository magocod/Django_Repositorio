## UNEFA Repository

> Digital repository, UNEFA internship project

## FRONT-END

* Bootstrap 4.1.0 -> https://getbootstrap.com/
* Materialize 1.0.0-beta -> http://materializecss.com/

```bash
#Next version

Vuejs -> https://github.com/magocod/Vue_repositorio

```

## BACK-END

* Django 2.0.4 -> https://www.djangoproject.com/
* Django-rest-framework 3.7.7-> http://www.django-rest-framework.org/
* Sqlite3 3.22.0 --> https://www.sqlite.org/index.html
* Postgresql 10.3 --> https://www.postgresql.org/

## Packages - Django

* django-cleanup==2.1.0
* django-unused-media==0.1.11
* django-debug-toolbar==1.9.1

## Packages - Python

* factory-boy==2.10.0 

## Javascript - Plugins

* Jquery 3.2.1
* Datatables 1.10.16
* Chosen 1.8.3

## Service Worker

* Workbox 3.1.0 --> https://developers.google.com/web/tools/workbox/ 

## Structure Directory
-------------------

      backend/             Information processing
             /account/     User control, profiles, permissions
             /api/         Exchange JSON, XML information
             /fabricator/  Enter test data
             /grabber/     Forms to enter data
             /seeker/      Search and filtering
             /storage/     Models and business logic
      kernel/              General page configuration
      static/              Static files
      templates/           HTML code
     
## instructions

install python virtual environment and install libraries with pip

```bash
pip install -r requirements.txt
```

Migrate the database

```bash
python manage.py migrate
```

Create User

```bash
python manage.py createsuperuser (name / email / password)
```

Enter test data with model factories 

```bash
python manage.py shell
```

Import model factories

```bash
from backend.fabricator.seeders import seederv2
s=seederv2
```

Enter quantities (numerical parameters) -> backend / fabricator / seeders.py

```bash
s.seed_1(t,ti) t=themes, ti=types of items 
s.seed_2(t,i,cl,ct) t=tags, i=items, cl=collections, ct=categories
```

Run development server

```bash
python manage.py runserver
```

Enter the address

```bash
http://localhost:8000
```
