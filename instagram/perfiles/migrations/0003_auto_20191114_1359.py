# Generated by Django 2.2.6 on 2019-11-14 18:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('perfiles', '0002_auto_20191114_1322'),
    ]

    operations = [
        migrations.AddField(
            model_name='comentario',
            name='foto_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='perfiles.Foto'),
        ),
        migrations.AddField(
            model_name='comentario',
            name='user_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='perfiles.Perfile'),
        ),
        migrations.AddField(
            model_name='foto',
            name='user_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='perfiles.Perfile'),
        ),
        migrations.AlterField(
            model_name='comentario',
            name='created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='comentario',
            name='modified',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='foto',
            name='created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='foto',
            name='modified',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('foto_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='perfiles.Foto')),
                ('user_id', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='perfiles.Perfile')),
            ],
        ),
    ]
