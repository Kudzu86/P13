from django.urls import reverse, resolve
from profiles.views import index, profile


def test_index_url():
    """Test pour vérifier que l'URL index des profils est correctement configurée."""
    url = reverse('profiles:index')
    assert url == '/profiles/'
    resolver = resolve(url)
    assert resolver.view_name == 'profiles:index'
    assert resolver.func == index


def test_profile_url():
    """Test pour vérifier que l'URL de détail d'un profil est correctement configurée."""
    url = reverse('profiles:profile', args=[1])
    assert url == '/profiles/1/'
    resolver = resolve(url)
    assert resolver.view_name == 'profiles:profile'
    assert resolver.func == profile
