Structure de la base de données
=============================

Architecture de la base de données
--------------------------------

L'application utilise SQLite en développement et est structurée autour de trois modèles principaux répartis dans deux applications Django.

Modèles de données
----------------

Application Lettings
~~~~~~~~~~~~~~~~~

.. code-block:: python

   # Modèle Address
   class Address(models.Model):
       number = models.PositiveIntegerField(validators=[MaxValueValidator(9999)])
       street = models.CharField(max_length=64)
       city = models.CharField(max_length=64)
       state = models.CharField(max_length=2, validators=[MinLengthValidator(2)])
       zip_code = models.PositiveIntegerField(validators=[MaxValueValidator(99999)])
       country_iso_code = models.CharField(max_length=3, validators=[MinLengthValidator(3)])
       
       def __str__(self):
           return f'{self.number} {self.street}'
           
   # Modèle Letting
   class Letting(models.Model):
       title = models.CharField(max_length=256)
       address = models.OneToOneField(Address, on_delete=models.CASCADE)
       
       def __str__(self):
           return self.title

Application Profiles
~~~~~~~~~~~~~~~~~

.. code-block:: python

   # Modèle Profile
   class Profile(models.Model):
       user = models.OneToOneField(User, on_delete=models.CASCADE)
       favorite_city = models.CharField(max_length=64, blank=True)
       
       def __str__(self):
           return self.user.username

Relations entre les modèles
-------------------------

* Une relation OneToOne entre ``User`` et ``Profile``
* Une relation OneToOne entre ``Address`` et ``Letting``

Schéma de la base de données
--------------------------

.. code-block::

   +----------------+       +---------------+       +---------------+
   |      User      |       |    Profile    |       |    Address    |
   +----------------+       +---------------+       +---------------+
   | id             |<----->| id            |       | id            |
   | username       |       | user_id       |       | number        |
   | email          |       | favorite_city |       | street        |
   | password       |       |               |       | city          |
   | ...            |       |               |       | state         |
   +----------------+       +---------------+       | zip_code      |
                                                   | country_iso    |
                                                   +---------------+
                                                          ^
                                                          |
                                                   +---------------+
                                                   |    Letting    |
                                                   +---------------+
                                                   | id            |
                                                   | title         |
                                                   | address_id    |
                                                   +---------------+
