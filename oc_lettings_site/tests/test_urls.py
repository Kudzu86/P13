from django.urls import reverse, resolve
from oc_lettings_site.views import index


def test_index_url():
    """Test pour vérifier que l'URL principale est correctement configurée."""
    url = reverse('index')
    assert url == '/'

    # Vérifier que l'URL est résolue vers la bonne vue
    resolver = resolve(url)
    assert resolver.view_name == 'index'
    assert resolver.func == index
