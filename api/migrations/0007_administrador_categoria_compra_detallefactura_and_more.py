# Generated by Django 4.0.4 on 2022-11-12 23:23

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_rutina_empleado'),
    ]

    operations = [
        migrations.CreateModel(
            name='Administrador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, validators=[django.core.validators.MinLengthValidator(3)])),
                ('apellido', models.CharField(max_length=50, validators=[django.core.validators.MinLengthValidator(3)])),
                ('correo', models.EmailField(max_length=254)),
                ('telefono', models.CharField(max_length=50, validators=[django.core.validators.MinLengthValidator(3)])),
            ],
        ),
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, validators=[django.core.validators.MinLengthValidator(3)])),
            ],
        ),
        migrations.CreateModel(
            name='Compra',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('valor', models.DecimalField(decimal_places=3, max_digits=10)),
                ('hora', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='DetalleFactura',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField(validators=[django.core.validators.MinValueValidator(1)])),
                ('precio', models.DecimalField(decimal_places=3, max_digits=10)),
                ('subtotal', models.DecimalField(decimal_places=3, max_digits=10)),
                ('descuento', models.DecimalField(decimal_places=3, max_digits=10)),
                ('total', models.DecimalField(decimal_places=3, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='DetallesOrden',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('precio', models.DecimalField(decimal_places=3, max_digits=10)),
                ('cantidad', models.IntegerField(validators=[django.core.validators.MinValueValidator(1)])),
            ],
        ),
        migrations.CreateModel(
            name='Devolucion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fechaDevolucion', models.DateField()),
                ('cantidad', models.IntegerField(validators=[django.core.validators.MinValueValidator(1)])),
                ('nombreProducto', models.CharField(max_length=50, validators=[django.core.validators.MinLengthValidator(3)])),
                ('razonDevolucion', models.CharField(max_length=50, validators=[django.core.validators.MinLengthValidator(3)])),
            ],
        ),
        migrations.CreateModel(
            name='Factura',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('hora', models.TimeField()),
                ('numeroFactura', models.IntegerField(validators=[django.core.validators.MinValueValidator(1)])),
            ],
        ),
        migrations.CreateModel(
            name='Impuesto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, validators=[django.core.validators.MinLengthValidator(3)])),
                ('valorImpuesto', models.DecimalField(decimal_places=3, max_digits=10)),
                ('fechaInicial', models.DateField()),
                ('fechaFinal', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='LoginAdministrador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('accion', models.CharField(max_length=50, validators=[django.core.validators.MinLengthValidator(3)])),
                ('informacion', models.CharField(max_length=50, validators=[django.core.validators.MinLengthValidator(3)])),
                ('fecha', models.DateField()),
                ('hora', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Orden',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fechaOrden', models.DateField()),
                ('fechaRequerida', models.DateField()),
                ('fechaEnvio', models.DateField()),
                ('direccionEnvio', models.CharField(max_length=100, validators=[django.core.validators.MinLengthValidator(3)])),
            ],
        ),
        migrations.CreateModel(
            name='ParametrosFactura',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cai', models.CharField(max_length=50, validators=[django.core.validators.MinLengthValidator(3)])),
                ('fechaEmision', models.DateField()),
                ('fechaVencimiento', models.DateField()),
                ('rangoInicial', models.IntegerField(validators=[django.core.validators.MinValueValidator(1)])),
                ('rangoFinal', models.IntegerField(validators=[django.core.validators.MinValueValidator(1)])),
                ('codigoSucursal', models.IntegerField(validators=[django.core.validators.MinValueValidator(1)])),
                ('ultimaFactura', models.IntegerField(validators=[django.core.validators.MinValueValidator(1)])),
            ],
        ),
        migrations.CreateModel(
            name='PrecioHistoricoProducto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fechaInicial', models.DateField()),
                ('fechaFinal', models.DateField()),
                ('precio', models.DecimalField(decimal_places=3, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigoProducto', models.IntegerField(validators=[django.core.validators.MinValueValidator(1)])),
                ('nombre', models.CharField(max_length=50, validators=[django.core.validators.MinLengthValidator(3)])),
                ('descripcion', models.CharField(max_length=100, validators=[django.core.validators.MinLengthValidator(3)])),
                ('cantidad', models.IntegerField(validators=[django.core.validators.MinValueValidator(1)])),
                ('cantidadMinima', models.IntegerField(validators=[django.core.validators.MinValueValidator(1)])),
            ],
        ),
    ]