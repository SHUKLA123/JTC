# Generated by Django 2.2 on 2020-01-25 04:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0002_contact_order'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='listing',
            new_name='product',
        ),
        migrations.RenameField(
            model_name='contact',
            old_name='listing_id',
            new_name='product_id',
        ),
    ]
