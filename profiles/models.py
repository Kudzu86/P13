"""Modèles pour la gestion des profils utilisateurs."""

from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    """Représente un profil utilisateur."""
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user_profile')
    favorite_city = models.CharField(max_length=64, blank=True)

    def __str__(self):
        """Retourne le nom d'utilisateur."""
        return self.user.username
