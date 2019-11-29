# Generated by Django 2.2.6 on 2019-11-29 18:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('perfiles', '0019_auto_20191129_0121'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='perfil',
            name='seguidores',
        ),
        migrations.CreateModel(
            name='Seguidores',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seguidor', models.IntegerField()),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('seguido', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='perfiles.Perfil')),
            ],
        ),
    ]
