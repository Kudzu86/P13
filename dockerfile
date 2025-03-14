FROM python:3.9-slim

# Définir les variables d'environnement
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Définir le répertoire de travail
WORKDIR /app

# Installer les dépendances
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copier le reste du code
COPY . .

# Collecter les fichiers statiques
RUN python manage.py collectstatic --noinput

# Commande par défaut pour exécuter l'application
CMD ["gunicorn", "--bind", "0.0.0.0:$PORT", "oc_lettings_site.wsgi:application"]
