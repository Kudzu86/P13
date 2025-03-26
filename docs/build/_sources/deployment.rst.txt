Procédures de déploiement
=======================

Architecture de déploiement
-------------------------

Le projet OC Lettings utilise un pipeline CI/CD complet avec les technologies suivantes :

* **GitHub Actions** pour l'automatisation des tests et du déploiement
* **Docker** pour la conteneurisation de l'application
* **Docker Hub** pour le stockage des images Docker
* **Render** pour l'hébergement de l'application

Pipeline CI/CD
------------

Le pipeline de déploiement est composé de trois tâches principales :

1. **Test** : Exécute les tests unitaires et vérifie la qualité du code
   * Lint avec flake8
   * Tests avec pytest
   * Vérification de la couverture de test (minimum 80%)

2. **Build and Push** : Crée et publie l'image Docker
   * Construction de l'image à partir du Dockerfile
   * Publication sur Docker Hub avec différents tags
   * Exécuté uniquement sur la branche master après réussite des tests

3. **Deploy** : Déploie l'application sur Render
   * Utilise l'API Render pour déclencher un déploiement
   * Exécuté uniquement sur la branche master après publication de l'image

Configuration requise
------------------

Pour configurer le pipeline CI/CD, vous devez :

1. **Créer un compte Docker Hub**
   * Créer un repository nommé "oc-lettings"
   * Générer un token d'accès personnel

2. **Créer un compte Render**
   * Configurer un service Web basé sur Docker
   * Obtenir l'ID du service et une clé API

3. **Configurer les secrets GitHub**
   * ``DOCKERHUB_USERNAME`` : Nom d'utilisateur Docker Hub
   * ``DOCKERHUB_TOKEN`` : Token d'accès Docker Hub
   * ``RENDER_API_KEY`` : Clé API Render
   * ``RENDER_SERVICE_ID`` : ID du service Render

4. **Configurer les variables d'environnement sur Render**
   * ``SECRET_KEY`` : Clé secrète Django
   * ``DEBUG`` : "False" en production
   * ``ALLOWED_HOSTS`` : Domaine Render et localhost
   * ``SENTRY_DSN`` : URL de connexion Sentry

Déploiement manuel et tests
-------------------------

**Déploiement via GitHub**

Pour déclencher un déploiement complet :

.. code-block:: bash

   git add .
   git commit -m "Votre message de commit"
   git push origin master

**Test de l'image Docker en local**

Pour tester l'image Docker localement :

.. code-block:: bash

   # Téléchargement de l'image
   docker pull kudzuu/oc-lettings:latest
   
   # Exécution de l'image
   docker run -p 8000:8000 \
      -e PORT=8000 \
      -e DEBUG=True \
      -e SECRET_KEY=your-secret-key \
      -e ALLOWED_HOSTS=localhost,127.0.0.1 \
      kudzuu/oc-lettings:latest

**Test de modification et redéploiement**

Pour tester le pipeline avec une modification simple :

1. Modifiez le titre dans un fichier template (par exemple, templates/index.html)
2. Commitez et poussez vos modifications sur la branche master
3. Vérifiez que le pipeline s'exécute correctement dans l'onglet Actions de GitHub
4. Vérifiez que le site déployé affiche les changements après quelques minutes

Surveillance et gestion des erreurs
---------------------------------

L'application utilise Sentry pour la surveillance des erreurs en production. Les erreurs et les logs importants sont automatiquement envoyés à Sentry.

Pour configurer Sentry :

1. Créez un compte sur Sentry.io
2. Créez un nouveau projet pour OC Lettings
3. Récupérez le DSN du projet
4. Ajoutez le DSN comme variable d'environnement sur Render
