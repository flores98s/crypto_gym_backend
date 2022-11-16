# Generated by Django 4.0.4 on 2022-11-16 04:11

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_rename_membresia_descuento_membresia_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='clave',
            field=models.CharField(max_length=100, validators=[django.core.validators.MinLengthValidator(3)]),
        ),
    ]
