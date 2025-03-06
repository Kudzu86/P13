import pytest
from django.urls import reverse
from django.test import Client
from django.contrib.auth.models import User
from profiles.models import Profile


@pytest.mark.django_db
def test_index_view():
    """Test pour vérifier que la page index des profils fonctionne correctement."""
    client = Client()
    url = reverse('profiles:index')
    response = client.get(url)

    assert response.status_code == 200
    assert b"Profiles" in response.content


@pytest.mark.django_db
def test_profile_view():
    """Test pour vérifier que la page de détail d'un profil fonctionne correctement."""
    # Créer un utilisateur et un profil pour le test
    user = User.objects.create_user(
        username="testuser",
        password="testpassword"
    )

    """la variable profile semble inutilisée MAIS,
    elle crée l'objet en base de données qui est ensuite récupéré via l'URL utilisant username"""
    profile = Profile.objects.create(  # noqa: F841
        user=user,
        favorite_city="Test City"
    )

    client = Client()
    url = reverse('profiles:profile', args=[user.username])
    response = client.get(url)

    assert response.status_code == 200
    assert b"testuser" in response.content
    assert b"Test City" in response.content


@pytest.mark.django_db
def test_profile_view_404():
    """Test pour vérifier que la page de détail d'un profil inexistant renvoie une 404."""
    client = Client()
    url = reverse('profiles:profile', args=[999])  # ID inexistant
    response = client.get(url)

    assert response.status_code == 404
