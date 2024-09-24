Liens disponibles : 
- http://localhost/weapons/(id) 
- http://localhost/inventory/(id)
- http://localhost/
- http://127.0.0.1/inventories/create/
- http://127.0.0.1/weapons/create/
- http://127.0.0.1/skins/create/
- http://localhost/api/data/
- http://localhost/api/inventaire/
- http://localhost/api/armes/
- http://localhost/api/skins/

Questions :



Partie I : Fonctionnement de Django

•	Vous disposez d'un projet Django dans lequel une application public a été créée. Décrivez la suite de requêtes et d'exécutions permettant l'affichage d'une page HTML index.html à l'URL global / via une application public, ne nécessitant pas de contexte de données. Vous décrirez la position exacte dans l'arborescence des répertoires des différents fichiers utiles à cette exécution.

Les différentes étapes :
1.	L'utilisateur saisit l'URL /.
2.	Une requête HTTP est envoyée au serveur Django.
3.	Django reçoit la requête et consulte le fichier myproject(nom_du_projet)/urls.py.
4.	Django redirige vers public/urls.py, qui fait correspondre l'URL à la vue correspondante.
5.	La vue qui se trouve dans public/views.py est appelée, qui rend le template associé.
6.	Django trouve le template, le compile et prépare une réponse HTTP.
7.	La réponse est envoyée au navigateur.
8.	Le navigateur affiche la page.


Dans quelle(s) section(s) de quel(s) fichier(s) peut-on configurer la base de données que l'on souhaite utiliser pour un projet Django ?
    Dans la section DATABASE du fichier settings.py

Dans quel(s) fichier(s) peut-on configurer le fichier de paramètres que l'on souhaite faire utiliser par le projet Django ? Si plusieurs fichers sont à mentionner, expliquez le rôle de chaque fichier.

    Les différents moyens : 
    1.	Manage.py : os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings'), La variable d'environnement DJANGO_SETTINGS_MODULE est définie ici, et elle indique le chemin vers le fichier de paramètres par défaut que Django doit utiliser.
    2.	wsgi.py : os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings') Tout comme dans manage.py, cette ligne configure la variable DJANGO_SETTINGS_MODULE pour que Django sache quel fichier de paramètres utiliser lors de l'exécution de l'application via le serveur WSGI (par exemple, Gunicorn ou uWSGI).
    3.	asgi.py : : os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings') Il configure la variable DJANGO_SETTINGS_MODULE pour indiquer quel fichier de paramètres utiliser dans les environnements asynchrones.

Nous nous plaçons à la racine de votre projet Django. Quel effet a l'exécution python manage.py makemigrations ? Et l'exécution python manage.py migrate ? Quel(s) fichier(s) sont mis en oeuvre pendant ces exécutions ?

1.	python manage.py makemigrations 
    Cette commande crée des fichiers de migration en fonction des modifications détectées dans les modèles de l'application Django.
    1.1 Effet de makemigrations :
    •	Création de migrations : Django inspecte les changements dans vos modèles (par exemple, la création d'un nouveau modèle, la modification des champs existants, ou la suppression d'un modèle) et génère des fichiers de migration correspondants.
    •	Fichiers générés : Django crée un nouveau fichier de migration pour chaque application où des changements ont été détectés. Ces fichiers se trouvent dans le répertoire migrations de chaque application.
    1.2 Exemple de fichier de migration généré :
    Si vous ajoutez un champ à un modèle (models.py) dans une application, un fichier de migration peut être généré dans myapp/migrations/. Chaque fichier de migration est numéroté de manière séquentielle (par exemple, 0001_initial.py pour la première migration, 0002_add_field_to_model.py pour la deuxième).
    1.3 Ce qui est mis en œuvre :
    •	Les modèles (définis dans models.py) sont inspectés par Django.
    •	Les fichiers de migration dans les répertoires migrations/ de chaque application sont créés ou mis à jour.

2.	python manage.py migrate 
    Cette commande applique les migrations créées par makemigrations à la base de données.
    2.1 Effet de migrate :
    •	Synchronisation avec la base de données : Django exécute les migrations générées par makemigrations en modifiant physiquement la base de données. Cela signifie que les tables sont créées, modifiées, ou supprimées selon les instructions des fichiers de migration.
    2.2 Fichiers impliqués par migrate :
    •	migrations/000x_<nom_migration>.py : Ces fichiers sont exécutés pour appliquer les modifications aux tables de la base de données.
    •	Base de données : La structure de la base de données est modifiée en fonction des instructions contenues dans les fichiers de migration.
    •	Table django_migrations : Cette table dans la base de données garde la trace des migrations qui ont été appliquées, en enregistrant le nom de chaque fichier de migration et son statut d'application.

Partie 2 : Fonctionnement de Docker
Expliquez l'effet et la syntaxe de ces commandes, communément vues dans des fichiers Dockerfile : FROM, RUN, WORKDIR, EXPOSE, CMD.

o	FROM : Indique l’image sur laquelle on va construire notre image personnalisée
o	RUN : Lance une à plusieurs commandes linux pendant la construction de l’image.
o	WORKDIR : Correspond en quelque sorte à l’équivalent de la commande « cd ». Donc au lancement du conteneur, on sera positionné dans le path indiqué dans WORKDIR.
o	EXPOSE : Indique de façon indicative seulement, le port sur lequel le conteneur écoute.
o	CMD : Spécifie le programme par défaut qui va être exécuté lors du lancement du conteneur.

Dans la définition d'un service dans le fichier docker-compose.yml, expliquez l'effet des mentions :
o	ports:
o	    - "80:80"
Cette configuration lie un port de l'hôte (la machine où Docker s'exécute) à un port du conteneur. Ici le port 80 de l'hôte est mappé au port 80 du conteneur.

o	build: 
o	    context: .
o	    dockerfile: Dockerfile.api

Cela signifie que Docker doit construire une image en utilisant les instructions contenues dans Dockerfile.api dans le répertoire courant (context : . ).

o	depends_on:
o	    - web
o	    - api

Cette configuration indique que le service actuel dépend des services web et api. Cela garantit que les services web et api sont démarrés avant le service qui dépend d'eux.

o	environment:
o	    POSTGRES_DB: ${POSTGRES_DB}
o	    POSTGRES_USER: ${POSTGRES_USER}
o	    POSTGRES_PASSWORD: ${POSTGRES_PASSWORD}

Cette section définit les variables d'environnement pour le service en question, ici pour une base de données PostgreSQL. Les valeurs de ces variables sont fournies via des variables externes définies dans un fichier .env ou dans l'environnement système où Docker Compose est exécuté.


•	Citez une méthode pour définir des variables d'environnement dans un conteneur.

    Une des méthodes pour définir des variables d’environnement est simplement dans le docker-compose d’ajouter « environment : » dans les services correspondants, afin de passer les variables d’environnement dès l’exécution du conteneur.

•	Dans un même réseau Docker, nous disposons d'un conteneur nginx (utilisant l'image nginx:latest) et d'un conteneur web (utilisant une image contenant un projet web Django, ayant la commande python manage.py runserver 0.0.0.0:8000 de lancée au démarrage du conteneur). Comment adresser le serveur web tournant dans le conteneur web depuis le conteneur nginx, sans utiliser les adresses IP des conteneurs ?

    Dans Docker, les conteneurs sur le même réseau peuvent se communiquer en utilisant leur nom de service ou nom de conteneur plutôt que les adresses IP. Cela permet de gérer les connexions de manière dynamique sans dépendre des adresses IP, qui peuvent changer.
