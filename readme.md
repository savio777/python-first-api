# python_first_api

### steps:

- init venv
- `pip install django`
- `django-admin startproject <name_project>`
- `python ./manage.py migrate`
- `python ./manage.py runserver`
- `python ./manage.py startapp <name_module>`
- add new module in `settings` -> `INSTALLED_APPS`
- add `views` views in `urls.py`
- create model in `models.py` and run `python ./manage.py makemigrations`
- run `python ./manage.py migrate` again

### steps for connect sql server:

- `pip install mssql-django`
- [config environment linux for driver sql](https://learn.microsoft.com/en-us/sql/connect/odbc/linux-mac/installing-the-microsoft-odbc-driver-for-sql-server?view=sql-server-ver16&tabs=alpine18-install%2Cubuntu17-install%2Cdebian8-install%2Credhat7-13-install%2Crhel7-offline)
- [config settings database api](https://learn.microsoft.com/en-us/samples/azure-samples/mssql-django-samples/mssql-django-samples/)

### plugins vscode:

- python
- black formatter
- docker

### docker used

`docker run -e "ACCEPT_EULA=Y" -e "MSSQL_SA_PASSWORD=12345Sa';" \
-p 1433:1433 --name sql1 --hostname sql1 \
-d \
mcr.microsoft.com/mssql/server:2022-latest`

### links

- [x] [Estrutura Básica de um Projeto em Django](https://www.youtube.com/watch?v=4u0aI-90KnU)
- [x] [DJANGO - Como CRIAR um Sistema de CADASTRO do ZERO!](https://www.youtube.com/watch?v=-m5ywU8SW9E)
- [ ] [Try Create Python API Rest](https://dev.to/brian101co/how-to-return-a-json-response-in-django-gen)
