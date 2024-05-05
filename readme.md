
---
# DjangoSweetCrud
# CRUD avec Django et SweetAlert 

Ce projet utilise Django pour implémenter les opérations CRUD (Create, Read, Update, Delete) et SweetAlert pour des boîtes de dialogue élégantes.

## Fonctionnalités

- **Create**: Permet aux utilisateurs d'ajouter de nouveaux articles à la base de données.
- **Read**: Affiche une liste des articles existants avec des détails.
- **Update**: Permet aux utilisateurs de modifier les articles existants.
- **Delete**: Permet aux utilisateurs de supprimer des articles de la base de données.

## Installation et Configuration

1. Clonez ce dépôt sur votre machine locale.
2. Installez les dépendances requises en exécutant `pip install -r requirements.txt`.
3. Configurez votre base de données dans le fichier `settings.py`.
4. Exécutez les migrations avec la commande `python manage.py migrate`.
5. Lancez le serveur de développement avec `python manage.py runserver`.

## Utilisation

1. Accédez à l'URL de votre projet dans votre navigateur.
2. Utilisez l'interface utilisateur pour ajouter, afficher, modifier ou supprimer des articles.
3. Les boîtes de dialogue SweetAlert seront utilisées pour confirmer les actions de création, de modification et de suppression.

## Exemples de Code

Vous pouvez trouver des exemples de code pour chaque opération CRUD dans les fichiers suivants:

- `views.py`: Contient les fonctions de vue pour gérer les requêtes HTTP.
- `templates/`: Contient les fichiers de modèle HTML pour afficher l'interface utilisateur.

[//]: # (- `static/js/`: Contient les fichiers JavaScript pour ajouter des fonctionnalités dynamiques, y compris l'utilisation de SweetAlert.)

## Contribuer

Si vous souhaitez contribuer à ce projet, veuillez suivre les instructions de [CONTRIBUTING.md](CONTRIBUTING.md).

## Licence

Ce projet est sous licence MIT - voir le fichier [LICENSE](LICENSE) pour plus de détails.

---


