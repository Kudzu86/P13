import pytest
from django.urls import reverse
from django.test import Client
from lettings.models import Address, Letting


@pytest.mark.django_db
def test_index_view():
    """Test pour vérifier que la page index des locations fonctionne correctement."""
    client = Client()
    url = reverse('lettings:index')
    response = client.get(url)

    assert response.status_code == 200
    assert b"Lettings" in response.content


@pytest.mark.django_db
def test_letting_view():
    """Test pour vérifier que la page de détail d'une location fonctionne correctement."""
    # Créer une adresse et une location pour le test
    address = Address.objects.create(
        number=123,
        street="Test Street",
        city="Test City",
        state="Test State",
        zip_code=12345,
        country_iso_code="US"
    )

    letting = Letting.objects.create(
        title="Test Letting",
        address=address
    )

    client = Client()
    url = reverse('lettings:letting', args=[letting.id])
    response = client.get(url)

    assert response.status_code == 200
    assert b"Test Letting" in response.content
    assert b"Test Street" in response.content


@pytest.mark.django_db
def test_letting_view_404():
    """Test pour vérifier que la page de détail d'une location inexistante renvoie une 404."""
    client = Client()
    url = reverse('lettings:letting', args=[999])  # ID inexistant
    response = client.get(url)

    assert response.status_code == 404
