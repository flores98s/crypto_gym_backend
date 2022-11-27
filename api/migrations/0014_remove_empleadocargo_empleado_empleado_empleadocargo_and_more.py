# Generated by Django 4.0.4 on 2022-11-25 04:57

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0013_alter_cliente_creado_alter_cliente_numerotelefono_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='empleadocargo',
            name='empleado',
        ),
        migrations.AddField(
            model_name='empleado',
            name='empleadoCargo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.empleadocargo'),
        ),
        migrations.AlterField(
            model_name='documentoempleado',
            name='nombreDocumento',
            field=models.CharField(max_length=50, validators=[django.core.validators.MinLengthValidator(3)]),
        ),
        migrations.AlterField(
            model_name='tipodocumentocliente',
            name='nombreDocumento',
            field=models.CharField(max_length=50, validators=[django.core.validators.MinLengthValidator(3)]),
        ),
        migrations.AlterField(
            model_name='tipogenero',
            name='nombre',
            field=models.CharField(max_length=50, validators=[django.core.validators.MinLengthValidator(3)]),
        ),
        migrations.AlterField(
            model_name='tiposangrecliente',
            name='nombreSangre',
            field=models.CharField(max_length=50, validators=[django.core.validators.MinLengthValidator(2)]),
        ),
    ]