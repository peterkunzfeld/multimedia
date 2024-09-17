# Generated by Django 5.1 on 2024-09-16 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('linksammlung', '0004_kategorien_description_subkategorien_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='autor',
            name='description',
            field=models.TextField(default='xxx'),
        ),
        migrations.AlterField(
            model_name='autor',
            name='url',
            field=models.URLField(default='xxx'),
        ),
        migrations.AlterField(
            model_name='kategorien',
            name='description',
            field=models.TextField(default='xxx'),
        ),
        migrations.AlterField(
            model_name='playlists',
            name='description',
            field=models.TextField(default='xxx'),
        ),
        migrations.AlterField(
            model_name='quelle',
            name='description',
            field=models.TextField(default='xxx'),
        ),
        migrations.AlterField(
            model_name='subkategorien',
            name='description',
            field=models.TextField(default='xxx'),
        ),
    ]
