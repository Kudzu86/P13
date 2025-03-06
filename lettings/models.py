"""Modèles pour la gestion des adresses et locations."""

from django.db import models
from django.core.validators import MaxValueValidator, MinLengthValidator


class Address(models.Model):
    """Représente une adresse physique."""
    number = models.PositiveIntegerField(validators=[MaxValueValidator(9999)])
    street = models.CharField(max_length=64)
    city = models.CharField(max_length=64)
    state = models.CharField(max_length=2, validators=[MinLengthValidator(2)])
    zip_code = models.PositiveIntegerField(validators=[MaxValueValidator(99999)])
    country_iso_code = models.CharField(max_length=3, validators=[MinLengthValidator(3)])

    class Meta:
        """Modifie correctement le mot 'Address' au pluriel"""
        verbose_name = "Address"
        verbose_name_plural = "Addresses"

    def __str__(self):
        """Retourne l'adresse au format 'numéro rue'."""
        return f'{self.number} {self.street}'


class Letting(models.Model):
    """Représente une location immobilière."""
    title = models.CharField(max_length=256)
    address = models.OneToOneField(Address, on_delete=models.CASCADE)

    def __str__(self):
        """Retourne le titre de la location."""
        return self.title
