# Generated by Django 2.2 on 2020-06-28 20:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recurso', '0002_auto_20200621_1938'),
        ('aula', '0005_aula_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='aula',
            name='discussoes',
            field=models.ManyToManyField(blank=True, related_name='discussoes', to='recurso.Recurso'),
        ),
    ]
