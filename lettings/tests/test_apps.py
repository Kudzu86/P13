from django.apps import apps
from lettings.apps import LettingsConfig


def test_app_config():
    """Test pour vérifier que la configuration de l'application est correcte."""
    assert LettingsConfig.name == 'lettings'
    app = apps.get_app_config('lettings')
    assert app.name == 'lettings'
