# Generated by Django 4.2.1 on 2023-05-19 21:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pharmacy',
            name='open_time',
            field=models.CharField(default='8.00am - 8.00pm ', max_length=20),
        ),
    ]