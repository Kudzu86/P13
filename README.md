# Orange County Lettings

## Résumé

Site web d'Orange County Lettings, une plateforme de location immobilière.

## Documentation

La documentation technique complète du projet est disponible sur [Read the Docs](https://p13-oc-lettings-auer-eric.readthedocs.io/).

## Développement local

### Prérequis

- Compte GitHub avec accès en lecture à ce repository
- Git CLI
- SQLite3 CLI
- Interpréteur Python, version 3.6 ou supérieure

Dans le reste de la documentation sur le développement local, il est supposé que la commande `python` de votre OS shell exécute l'interpréteur Python ci-dessus (à moins qu'un environnement virtuel ne soit activé).

### macOS / Linux

#### Cloner le repository

- `cd /path/to/put/project/in`
- `git clone https://github.com/OpenClassrooms-Student-Center/Python-OC-Lettings-FR.git`

#### Créer l'environnement virtuel

- `cd /path/to/Python-OC-Lettings-FR`
- `python -m venv venv`
- `apt-get install python3-venv` (Si l'étape précédente comporte des erreurs avec un paquet non trouvé sur Ubuntu)
- Activer l'environnement `source venv/bin/activate`
- Confirmer que la commande `python` exécute l'interpréteur Python dans l'environnement virtuel
`which python`
- Confirmer que la version de l'interpréteur Python est la version 3.6 ou supérieure `python --version`
- Confirmer que la commande `pip` exécute l'exécutable pip dans l'environnement virtuel, `which pip`
- Pour désactiver l'environnement, `deactivate`

#### Exécuter le site

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `pip install --requirement requirements.txt`
- `python manage.py runserver`
- Aller sur `http://localhost:8000` dans un navigateur.
- Confirmer que le site fonctionne et qu'il est possible de naviguer (vous devriez voir plusieurs profils et locations).

#### Linting

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `flake8`

#### Tests unitaires

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `pytest`

#### Base de données

- `cd /path/to/Python-OC-Lettings-FR`
- Ouvrir une session shell `sqlite3`
- Se connecter à la base de données `.open oc-lettings-site.sqlite3`
- Afficher les tables dans la base de données `.tables`
- Afficher les colonnes dans le tableau des profils, `pragma table_info(Python-OC-Lettings-FR_profile);`
- Lancer une requête sur la table des profils, `select user_id, favorite_city from Python-OC-Lettings-FR_profile where favorite_city like 'B%';`
- `.quit` pour quitter

#### Panel d'administration

- Aller sur `http://localhost:8000/admin`
- Connectez-vous avec l'utilisateur `admin`, mot de passe `Abc1234!`

### Windows

Utilisation de PowerShell, comme ci-dessus sauf :

- Pour activer l'environnement virtuel, `.\venv\Scripts\Activate.ps1` 
- Remplacer `which <my-command>` par `(Get-Command <my-command>).Path`

## Déploiement

### Récapitulatif du fonctionnement

Cette application utilise GitHub Actions pour automatiser le processus CI/CD:
1. Tests et linting à chaque push ou pull request
2. Construction et publication d'une image Docker sur Docker Hub (branche master uniquement)
3. Déploiement automatique sur Render.com (branche master uniquement)

### Configuration requise

Pour que le déploiement fonctionne correctement, vous devez configurer:
- Un compte Docker Hub avec un repository nommé "oc-lettings"
- Un service Web sur Render.com configuré pour déployer l'application
- Les secrets GitHub suivants:
  - DOCKERHUB_USERNAME: votre nom d'utilisateur Docker Hub
  - DOCKERHUB_TOKEN: votre token d'accès Docker Hub
  - RENDER_API_KEY: votre clé API Render
  - RENDER_SERVICE_ID: l'identifiant de votre service sur Render

### Variables d'environnement sur Render.com

Pour que l'application fonctionne correctement en production, configurez les variables d'environnement suivantes sur Render:
- SECRET_KEY: une clé secrète pour Django
- DEBUG: "False"
- ALLOWED_HOSTS: votre-app.onrender.com,localhost,127.0.0.1
- SENTRY_DSN: votre DSN Sentry (si surveillance Sentry configurée)

### Étapes de déploiement

#### Déploiement automatique
1. Faites vos modifications
2. Validez et poussez votre code sur la branche master
3. GitHub Actions exécutera automatiquement les tests, construira l'image, la publiera sur Docker Hub et déploiera sur Render

#### Déploiement manuel
Pour extraire et exécuter l'image Docker en local:
```bash
# Extraire l'image depuis Docker Hub
docker pull kudzuu/oc-lettings:latest

# Exécuter l'image
docker run -p 8000:8000 -e PORT=8000 -e DEBUG=True -e SECRET_KEY=your-secret-key -e ALLOWED_HOSTS=localhost,127.0.0.1 kudzuu/oc-lettings:latest
