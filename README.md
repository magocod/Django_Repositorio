## UNEFA Repository

> Digital repository, UNEFA internship project

## Framework

* Django 2.2.2 -> https://www.djangoproject.com/

## Database

* Sqlite3 3.22.0 --> https://www.sqlite.org/index.html
* Postgresql 10.3 --> https://www.postgresql.org/

## Packages - Django

* Django-rest-framework 3.7.7-> http://www.django-rest-framework.org/
* django-unused-media==0.1.11

## instructions

install python virtual environment and install libraries with pip

```bash
pip install -r requirements.txt
```

Migrate the database

```bash
python manage.py migrate
```

Create Users

```bash
python manage.py USeeders
```

Run development server

```bash
python manage.py runserver
```

Enter the address

```bash
http://localhost:8000
```
