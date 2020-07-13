# Generated by Django 2.2.4 on 2020-07-13 20:09

from django.db import migrations

def link_flats_with_owners(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    Owner = apps.get_model('property', 'Owner')
    for flat in Flat.objects.all():
        owner, created = Owner.objects.get_or_create(full_name=flat.owner, phonenumber=flat.owners_phonenumber)
        owner.own_flats.add(flat)


def move_backward(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    Owner = apps.get_model('property', 'Owner')
    for flat in Flat.objects.all():
        owner, created = Owner.objects.update_or_create(full_name=flat.owner, phonenumber=flat.owners_phonenumber)
        owner.flat_set.clear()

class Migration(migrations.Migration):

    dependencies = [
        ('property', '0016_auto_20200713_2309'),
    ]

    operations = [
        migrations.RunPython(link_flats_with_owners, move_backward),
    ]