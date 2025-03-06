"""Configuration de l'admin pour les modèles de location."""

from django.contrib import admin
from .models import Address, Letting


admin.site.register(Address)
admin.site.register(Letting)
