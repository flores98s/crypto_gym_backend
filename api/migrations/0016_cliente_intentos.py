# Generated by Django 4.0.4 on 2022-11-28 02:30

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0015_remove_categoria_producto_remove_descuento_cliente_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='intentos',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(1)]),
        ),
    ]
