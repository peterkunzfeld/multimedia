# Generated by Django 5.1 on 2024-09-16 11:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('linksammlung', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubKategorie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('kategorie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='linksammlung.kategorie')),
            ],
        ),
    ]
