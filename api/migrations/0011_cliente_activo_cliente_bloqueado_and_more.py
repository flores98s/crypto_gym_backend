# Generated by Django 4.0.4 on 2022-11-19 04:15

import api.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_alter_cliente_clave'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='activo',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='cliente',
            name='bloqueado',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='fechaNacimiento',
            field=models.DateField(validators=[api.validators.validate_fecha]),
        ),
    ]
