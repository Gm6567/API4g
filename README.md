## Sommaire
1. [Résumé](#Résumé)
2. [Exemples d'utilisation](#Exemples-dutilisation)
3. [Conteneurisation des services](#Conteneurisation-des-services)
4. [La base de données](#La-base-de-données)
5. [Lancer l'application](#Lancer-lapplication)


## Résumé

Ce repository est composé d'un backend python (Django rest) qui expose une route POST, d'un front-end Angular qui requête la route POST de l'API.
La base de données de l'API est une base de données PostgreSQL.


### Exemples d'utilisation
#### Exemple d'utilisation de la route POST via l'API
<img width="1433" height="863" alt="image" src="https://github.com/user-attachments/assets/4fdc21b6-0df2-49fa-b543-ea8bb558e28e" />



#### Exemple de l'utilisation du front-end Angular
<img width="923" height="235" alt="image" src="https://github.com/user-attachments/assets/eb6dd9d4-fedf-44d8-8006-bd7cd98d4d61" />

### Conteneurisation des services

Le fichier Docker-compose.yml définit 3 conteneurs dans cet ordre:
- Un pour la base de données PostgreSQL
- Un pour l'API Django rest
- Un pour le front-end Angular

### La base de données
La base de données est définie dans un premier temps (avec l'extension postgis utile pour le calcul de distance entre plusieurs longitudes et latitudes), puis est remplie lors de la création du container django grâce à l'éxecution du script get_data_from_csv.py qui se situe dans le dossier ../addressApplication/management
/commands.
Les coordonnées x et y présents dans le fichier data_operator.csv sont remplacés par la latitude et la longitude dans la base de données PostgreSQL (grâce au module pyproj).

### Lancer l'application
Il faut avoir Docker compose installé sur sa machine et lancer la commande suivante : ```docker compose up --build``` 
dans un terminal depuis la racine de l'application où se situe le fichier docker-compose.yml


