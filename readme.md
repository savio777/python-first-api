# python_first_api

![alt text](./imgs/doc-ex.png)

### steps

- init venv
- `pip install django djangorestframework django-cors-headers`
- `django-admin startproject <name_project>`
- add new module in `settings` -> `INSTALLED_APPS` and configs of `cors` and `djangorestframework`
- create models
- `python ./manage.py makemigrations`
- `python ./manage.py migrate`
- register model in `admin.py`
- `python ./manage.py createsuperuser`
- `python ./manage.py runserver`
- `python ./manage.py startapp <name_module>`
- create `serializers.py`
- create `views` and add views in `urls.py`
- test in browser `http://127.0.0.1:8000/api/users/?format=api`

### requirements

- create requirements: `pip freeze > requirements.txt`
- after create venv: `pip install -r requirements.txt`

### the next time you run

- `pip install --force-reinstall -U setuptools`
- `pip install -r requirements.txt`

### steps for connect sql server

- `pip install mssql-django`
- [config environment linux for driver sql](https://learn.microsoft.com/en-us/sql/connect/odbc/linux-mac/installing-the-microsoft-odbc-driver-for-sql-server?view=sql-server-ver16&tabs=alpine18-install%2Cubuntu17-install%2Cdebian8-install%2Credhat7-13-install%2Crhel7-offline)
- [config settings database api](https://learn.microsoft.com/en-us/samples/azure-samples/mssql-django-samples/mssql-django-samples/)

### plugins vscode

- python
- black formatter
- docker

### docker used

`docker run -e "ACCEPT_EULA=Y" -e "MSSQL_SA_PASSWORD=12345Sa';" \
-p 1433:1433 --name sql1 --hostname sql1 \
-d \
mcr.microsoft.com/mssql/server:2022-latest`

### structure files ex

![files](./imgs/structure-files.png)

### version pip

```
asgiref==3.8.1
certifi==2024.2.2
charset-normalizer==3.3.2
coreapi==2.3.3
coreschema==0.0.4
Django==5.0.6
django-cors-headers==4.3.1
djangorestframework==3.15.1
drf-yasg==1.21.7
idna==3.7
inflection==0.5.1
itypes==1.2.0
Jinja2==3.1.4
MarkupSafe==2.1.5
mssql-django==1.5
openapi-codec==1.3.2
packaging==24.0
pyodbc==5.1.0
pytz==2024.1
PyYAML==6.0.1
requests==2.32.2
setuptools==70.0.0
simplejson==3.19.2
sqlparse==0.5.0
typing_extensions==4.11.0
uritemplate==4.1.1
urllib3==2.2.1
```

### links

- [x] [Estrutura Básica de um Projeto em Django](https://www.youtube.com/watch?v=4u0aI-90KnU)
- [x] [DJANGO - Como CRIAR um Sistema de CADASTRO do ZERO!](https://www.youtube.com/watch?v=-m5ywU8SW9E)
- [x] [Try Create Python API Rest](https://dev.to/brian101co/how-to-return-a-json-response-in-django-gen)
- [x] [Como criar uma API em Django - Criando um CRUD - Aula Completa](https://www.youtube.com/watch?v=Q2tEqNfgIXM)
