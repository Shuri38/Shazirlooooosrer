#!/bin/bash

python ./django-site/webdev/manage.py makemigrations #Regarde les migrations
python ./django-site/webdev/manage.py migrate  # Appliquer les migrations
python ./django-site/webdev/manage.py runserver 0.0.0.0:8000 --settings=webdev.settings.public  # Lancer le serveur sur tous les réseaux