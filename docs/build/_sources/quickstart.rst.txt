Guide de démarrage rapide
========================

Ce guide vous permet de lancer rapidement l'application et de comprendre sa structure.

Lancement de l'application
-------------------------

1. Activez l'environnement virtuel :

   .. code-block:: bash

      # Linux/macOS
      source venv/bin/activate
      
      # Windows
      .\venv\Scripts\activate

2. Lancez le serveur de développement :

   .. code-block:: bash

      python manage.py runserver

3. Accédez à l'application dans votre navigateur à l'adresse : http://127.0.0.1:8000/

Navigation dans l'application
---------------------------

* **Page d'accueil** : `/`
* **Liste des locations** : `/lettings/`
* **Détails d'une location** : `/lettings/<id>/`
* **Liste des profils** : `/profiles/`
* **Détail d'un profil** : `/profiles/<username>/`

Utilisation du panneau d'administration
-------------------------------------

1. Accédez à l'interface d'administration : http://127.0.0.1:8000/admin/
2. Connectez-vous avec les identifiants administrateur (par défaut : admin/Abc1234!)
3. Gérez les utilisateurs, les profils et les locations depuis cette interface
