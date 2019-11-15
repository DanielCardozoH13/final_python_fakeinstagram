# Generated by Django 2.2.6 on 2019-11-14 19:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('perfiles', '0003_auto_20191114_1359'),
    ]

    operations = [
        migrations.CreateModel(
            name='Seguidor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('followed_user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Seguidor', to='perfiles.Perfile')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Seguido', to='perfiles.Perfile')),
            ],
        ),
        migrations.AddField(
            model_name='perfile',
            name='seguidores',
            field=models.ManyToManyField(through='perfiles.Seguidor', to='perfiles.Perfile'),
        ),
    ]
