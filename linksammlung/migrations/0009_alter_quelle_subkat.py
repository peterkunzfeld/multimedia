# Generated by Django 5.1 on 2024-09-16 14:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('linksammlung', '0008_alter_quelle_subkat'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quelle',
            name='subkat',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='linksammlung.subkategorien'),
        ),
    ]
