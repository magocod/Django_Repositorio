## UNEFA Repository

> Python 3.8
> Digital repository, UNEFA internship project

## Tox env

* Python 3.7
* Python 3.8
* Python lint flake8 (py3.8)

## Framework

* Django 3.0.0 -> https://www.djangoproject.com/

## Database

* Sqlite3 --> https://www.sqlite.org/index.html
* Postgresql --> https://www.postgresql.org/

## Third Packages

* Django-rest-framework 3.11.0 --> http://www.django-rest-framework.org/
* django-unused-media --> 0.1.11

## Tests

* Python unittest -> https://docs.python.org/3/library/unittest.html
* Django tests -> https://docs.djangoproject.com/en/3.0/topics/testing/

## instructions

install python virtual environment and install libraries with pip

```bash
pip install -r requirements.txt
```

Migrate the database

```bash
python manage.py migrate
```

Run development server

```bash
python manage.py runserver
```

Enter the address

```bash
http://localhost:8000
```
