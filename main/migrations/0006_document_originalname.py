# Generated by Django 3.0.5 on 2020-05-30 01:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_document_isfinished'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='originalName',
            field=models.CharField(default='Not set', max_length=256),
            preserve_default=False,
        ),
    ]
