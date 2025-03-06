import pytest
from django.contrib.auth.models import User
from profiles.models import Profile


@pytest.mark.django_db
def test_profile_creation():
    """Test pour vérifier la création d'un objet Profile."""
    user = User.objects.create_user(
        username="testuser",
        password="testpassword"
    )

    profile = Profile.objects.create(
        user=user,
        favorite_city="Test City"
    )

    assert profile.user == user
    assert profile.favorite_city == "Test City"


@pytest.mark.django_db
def test_profile_str():
    """Test pour vérifier la méthode __str__ du modèle Profile."""
    user = User.objects.create_user(
        username="testuser",
        password="testpassword"
    )

    profile = Profile.objects.create(
        user=user,
        favorite_city="Test City"
    )

    assert str(profile) == "testuser"
