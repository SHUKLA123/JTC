# Generated by Django 2.2 on 2020-01-27 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0005_remove_contact_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='order',
            field=models.BooleanField(default=False),
        ),
    ]
