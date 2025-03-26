Installation du projet
=====================

Prérequis
--------

* Compte GitHub avec accès en lecture au repository
* Git
* SQLite3
* Python 3.6 ou supérieur
* Pip (gestionnaire de paquets Python)

Étapes d'installation
-------------------

1. Cloner le dépôt GitHub :

   .. code-block:: bash

      git clone https://github.com/Kudzu86/P13
      cd oc-lettings-site

2. Créer et activer un environnement virtuel :

   .. code-block:: bash

      # Pour Linux/macOS
      python -m venv venv
      source venv/bin/activate
      
      # Pour Windows
      python -m venv venv
      .\venv\Scripts\activate

3. Installer les dépendances :

   .. code-block:: bash

      pip install -r requirements.txt

4. Appliquer les migrations :

   .. code-block:: bash

      python manage.py migrate

5. Créer un superutilisateur (facultatif) :

   .. code-block:: bash

      python manage.py createsuperuser

Configuration des variables d'environnement
-----------------------------------------

Créez un fichier `.env` à la racine du projet avec les variables suivantes :

.. code-block:: text

   SECRET_KEY=your_secret_key_here
   DEBUG=True
   ALLOWED_HOSTS=localhost,127.0.0.1
   SENTRY_DSN=your_sentry_dsn_here
