"""Vues de l'application principale."""

import logging
from django.shortcuts import render


logger = logging.getLogger('oc_lettings_site')


def index(request):
    """Affiche la page d'accueil."""
    logger.info('Page d\'accueil visitée')
    return render(request, 'index.html')
