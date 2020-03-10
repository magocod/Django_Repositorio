UNEFA Repository
================
![Alt text](https://firebasestorage.googleapis.com/v0/b/django-237201.appspot.com/o/repo_tags%2Ftag_py_36_37.png?alt=media&token=54c1a277-f100-4e47-b5a7-09afe86c3550 "python_versions")
![Alt text](https://firebasestorage.googleapis.com/v0/b/django-237201.appspot.com/o/repo_tags%2Fcode_style_black.svg?alt=media&token=c4090132-fde3-4fb3-9e96-4e13d19bc1fb "code_style")

Digital repository, UNEFA internship project

* Demo url: https://djrepo.herokuapp.com/

## Tox env

* Python 3.7
* Python 3.8
* Python lint flake8 (py3.8)

## Framework

* Django -> https://www.djangoproject.com/

## Database

* Sqlite3 -> https://www.sqlite.org/index.html
* Postgresql -> https://www.postgresql.org/

## Third Packages

* Django-rest-framework -> http://www.django-rest-framework.org/
* black -> https://black.readthedocs.io/en/stable/
* isort -> https://timothycrosley.github.io/isort/
* django-unused-media

## Tests (99% coverage)

* Python unittest -> https://docs.python.org/3/library/unittest.html
* Django tests -> https://docs.djangoproject.com/en/3.0/topics/testing/
* coverage -> https://coverage.readthedocs.io/en/coverage-5.0.3/

## instructions

Create a virtual python environment and install libraries with pip

```bash
pip install -r requirements.txt
```

Create all virtual environments (using tox)
```bash
tox
```

Migrate the database

```bash
python manage.py migrate
```

run tests (verify successful installation)
```bash
python manage.py test
```

run tests (verify coverage)
```bash
coverage run --source='.' manage.py test
coverage report
```

Run development server

```bash
python manage.py runserver
```

Enter the address

```bash
http://localhost:8000
```
