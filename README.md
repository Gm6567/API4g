## API4G

Ce repository est composé d'un backend python (Django rest) qui expose une route POST, d'un front-end Angular qui requête la route POST de l'API.
La base de données de l'API est une base de données PostgreSQL.



### Exemple d'utilisation de la route POST via l'API
<img width="1433" height="863" alt="image" src="https://github.com/user-attachments/assets/4fdc21b6-0df2-49fa-b543-ea8bb558e28e" />



### Exemple de l'utilisation du front-end Angular
<img width="923" height="235" alt="image" src="https://github.com/user-attachments/assets/eb6dd9d4-fedf-44d8-8006-bd7cd98d4d61" />

### Containerisation des services

Le fichier Docker-compose.yml définit 3 conteneurs dans cet ordre:
- Un pour la base de données PostgreSQL
- Un pour l'API Django rest
- Un pour le front-end Angular
La base de données est définie dans un premier temps (avec l'extension postgis utile pour le calcul de distance entre plusieurs longitudes et latitudes), puis est remplie lors de la création du container django grâce à l'éxecution d'un script (../addressApplication/get_data_from_csv.py) 

