# Generated by Django 5.1.3 on 2025-03-11 10:05

import tinymce.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('plaintes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='faq',
            name='reponse',
            field=tinymce.models.HTMLField(),
        ),
    ]
