from django.urls import reverse
from django.test import Client


def test_index_view():
    """Test pour vérifier que la page d'accueil principale fonctionne correctement."""
    client = Client()
    url = reverse('index')
    response = client.get(url)

    assert response.status_code == 200
    # Vérifier le contenu de base de la page d'accueil
    assert b"Welcome to Holiday Homes" in response.content
