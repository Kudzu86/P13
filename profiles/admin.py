"""Configuration de l'admin pour les profils."""

from django.contrib import admin
from .models import Profile


admin.site.register(Profile)
