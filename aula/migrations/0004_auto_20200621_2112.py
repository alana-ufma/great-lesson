# Generated by Django 2.2 on 2020-06-22 00:12

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aula', '0003_auto_20200621_2002'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aula',
            name='descricao',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='Descricao'),
        ),
    ]