# Generated by Django 2.2.6 on 2019-11-28 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perfiles', '0013_foto_is_historia'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='like',
            name='foto_id',
        ),
        migrations.AddField(
            model_name='foto',
            name='likes',
            field=models.ManyToManyField(to='perfiles.Like'),
        ),
    ]
