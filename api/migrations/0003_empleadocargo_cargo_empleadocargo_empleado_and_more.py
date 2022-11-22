# Generated by Django 4.0.4 on 2022-11-12 05:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_asignacionrutina_capacidad_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='empleadocargo',
            name='cargo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.cargo'),
        ),
        migrations.AddField(
            model_name='empleadocargo',
            name='empleado',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.empleado'),
        ),
        migrations.AddField(
            model_name='planilla',
            name='DetallePlanilla',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.detalleplanilla'),
        ),
        migrations.AddField(
            model_name='planilla',
            name='empleado',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.empleado'),
        ),
    ]