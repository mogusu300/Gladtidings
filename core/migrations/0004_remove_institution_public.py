# Generated by Django 5.0.4 on 2024-10-03 13:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_institution_public'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='institution',
            name='public',
        ),
    ]