# Generated by Django 2.2.6 on 2019-11-16 05:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('noticias', '0004_auto_20191114_1322'),
    ]

    operations = [
        migrations.AddField(
            model_name='noticia',
            name='user',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
