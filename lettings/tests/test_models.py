import pytest
from lettings.models import Address, Letting


@pytest.mark.django_db
def test_address_creation():
    """Test pour vérifier la création d'un objet Address."""
    address = Address.objects.create(
        number=123,
        street="Test Street",
        city="Test City",
        state="Test State",
        zip_code=12345,
        country_iso_code="US"
    )

    assert address.number == 123
    assert address.street == "Test Street"
    assert address.city == "Test City"
    assert address.state == "Test State"
    assert address.zip_code == 12345
    assert address.country_iso_code == "US"


@pytest.mark.django_db
def test_address_str():
    """Test pour vérifier la méthode __str__ du modèle Address."""
    address = Address.objects.create(
        number=123,
        street="Test Street",
        city="Test City",
        state="Test State",
        zip_code=12345,
        country_iso_code="US"
    )

    assert str(address) == "123 Test Street"


@pytest.mark.django_db
def test_letting_creation():
    """Test pour vérifier la création d'un objet Letting."""
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

    assert letting.title == "Test Letting"
    assert letting.address == address


@pytest.mark.django_db
def test_letting_str():
    """Test pour vérifier la méthode __str__ du modèle Letting."""
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

    assert str(letting) == "Test Letting"
