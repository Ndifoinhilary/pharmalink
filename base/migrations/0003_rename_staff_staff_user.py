# Generated by Django 4.2.1 on 2023-05-20 22:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_pharmacy_open_time'),
    ]

    operations = [
        migrations.RenameField(
            model_name='staff',
            old_name='staff',
            new_name='user',
        ),
    ]
