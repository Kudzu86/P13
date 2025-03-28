from django.db import migrations


def copy_data(apps, schema_editor):
    OldAddress = apps.get_model('oc_lettings_site', 'Address')
    NewAddress = apps.get_model('lettings', 'Address')
    OldLetting = apps.get_model('oc_lettings_site', 'Letting')
    NewLetting = apps.get_model('lettings', 'Letting')
    
    # Copier les adresses
    for old_address in OldAddress.objects.all():
        new_address = NewAddress(
            id=old_address.id,
            number=old_address.number,
            street=old_address.street,
            city=old_address.city,
            state=old_address.state,
            zip_code=old_address.zip_code,
            country_iso_code=old_address.country_iso_code
        )
        new_address.save()
    
    # Copier les locations
    for old_letting in OldLetting.objects.all():
        new_letting = NewLetting(
            id=old_letting.id,
            title=old_letting.title,
            address_id=old_letting.address_id
        )
        new_letting.save()

class Migration(migrations.Migration):
    dependencies = [
        ('lettings', '0001_initial'),
        ('oc_lettings_site', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(copy_data),
    ]