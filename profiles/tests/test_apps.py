from django.apps import apps
from profiles.apps import ProfilesConfig


def test_app_config():
    """Test pour vérifier que la configuration de l'application est correcte."""
    assert ProfilesConfig.name == 'profiles'
    app = apps.get_app_config('profiles')
    assert app.name == 'profiles'
