#Download Python
https://www.python.org/downloads

#Criar alias para terminal
alias python='python3'

#Jupiter servidor e compilador python
http://jupyter.org/install

#Exemplo Flask
pip3 install flask flask-sqlalchemy dataset

#Exemplo Django
pip3 install django

#PostgreSQL
pip3 install psycopg2

#Criar projeto Django
django-admin startproject mysite


##Migração
python manage.py makemigrations
python manage.py migrate

##Executar servidor

python manage.py runserver

##Consultas
python manage.py shell

Noticia.objects.create(titulo='titulo', conteudo='conteudo')
categoria = Categoria(titulo='titulo', descricao='texto')


##Admin Django
python manage.py createsuperuser