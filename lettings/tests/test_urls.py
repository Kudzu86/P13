from django.urls import reverse, resolve
from lettings.views import index, letting


def test_index_url():
    """Test pour vérifier que l'URL index des locations est correctement configurée."""
    url = reverse('lettings:index')
    assert url == '/lettings/'
    resolver = resolve(url)
    assert resolver.view_name == 'lettings:index'
    assert resolver.func == index


def test_letting_url():
    """Test pour vérifier que l'URL de détail d'une location est correctement configurée."""
    url = reverse('lettings:letting', args=[1])
    assert url == '/lettings/1/'
    resolver = resolve(url)
    assert resolver.view_name == 'lettings:letting'
    assert resolver.func == letting
