# Generated by Django 2.2.6 on 2019-11-16 05:07

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('perfiles', '0004_auto_20191114_1424'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Perfile',
            new_name='Perfil',
        ),
    ]
