"""Vues pour l'affichage des locations."""
import logging
from django.shortcuts import render, get_object_or_404
from lettings.models import Letting


logger = logging.getLogger('lettings')


def index(request):
    """Affiche la liste de toutes les locations."""
    logger.info('Page de liste des locations visitée')
    lettings_list = Letting.objects.all()
    context = {'lettings_list': lettings_list}
    return render(request, 'lettings/index.html', context)


def letting(request, letting_id):
    """Affiche les détails d'une location spécifique."""
    letting = get_object_or_404(Letting, id=letting_id)
    logger.info(f'Détails de la location {letting_id} consultés')
    context = {
        'title': letting.title,
        'address': letting.address,
    }
    return render(request, 'lettings/letting.html', context)
