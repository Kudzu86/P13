"""Vues pour l'affichage des profils utilisateurs."""
import logging
from django.shortcuts import render, get_object_or_404
from profiles.models import Profile


logger = logging.getLogger('profiles')


def index(request):
    """Affiche la liste de tous les profils."""
    logger.info('Page de liste des profils visitée')
    profiles_list = Profile.objects.all()
    context = {'profiles_list': profiles_list}
    return render(request, 'profiles/index.html', context)


def profile(request, username):
    """Affiche les détails d'un profil spécifique."""
    profile = get_object_or_404(Profile, user__username=username)
    logger.info(f'Profil de {username} consulté')
    context = {'profile': profile}
    return render(request, 'profiles/profile.html', context)
