# Generated by Django 4.2 on 2023-04-28 10:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sustainable_products',
            old_name='reference_links',
            new_name='reference_link',
        ),
    ]
