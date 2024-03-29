# Generated by Django 4.0.4 on 2023-03-25 02:26

import api.validators
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Administrador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, validators=[django.core.validators.MinLengthValidator(3), api.validators.validate_nombre])),
                ('apellido', models.CharField(max_length=50, validators=[django.core.validators.MinLengthValidator(3), api.validators.validate_nombre])),
                ('correo', models.EmailField(max_length=254)),
                ('telefono', models.CharField(max_length=50, validators=[django.core.validators.MinLengthValidator(3), api.validators.validate_nombre])),
            ],
        ),
        migrations.CreateModel(
            name='AsignacionDieta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField(validators=[api.validators.validate_fecha])),
                ('hora', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='AsignacionRutina',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('series', models.IntegerField(validators=[django.core.validators.MinValueValidator(0)])),
                ('repeticiones', models.IntegerField(validators=[django.core.validators.MinValueValidator(0)])),
                ('descanso', models.IntegerField(validators=[django.core.validators.MinValueValidator(0)])),
                ('capacidad', models.IntegerField(validators=[django.core.validators.MinValueValidator(0)])),
            ],
            options={
                'verbose_name_plural': 'Asignaciones Rutinas',
            },
        ),
        migrations.CreateModel(
            name='Cargo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreCargo', models.CharField(max_length=50, validators=[django.core.validators.MinLengthValidator(3), api.validators.validate_nombre])),
                ('salario', models.DecimalField(decimal_places=3, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, validators=[django.core.validators.MinLengthValidator(3), api.validators.validate_nombre])),
            ],
        ),
        migrations.CreateModel(
            name='ClaseGrupal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreClase', models.CharField(max_length=50, validators=[django.core.validators.MinLengthValidator(3), api.validators.validate_nombre])),
                ('cantidadAlumnos', models.IntegerField(validators=[django.core.validators.MinValueValidator(1)])),
            ],
            options={
                'verbose_name_plural': 'Clases Grupales',
            },
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombres', models.CharField(max_length=50, validators=[django.core.validators.MinLengthValidator(2), api.validators.validate_nombre])),
                ('apellidos', models.CharField(max_length=50, validators=[django.core.validators.MinLengthValidator(2), api.validators.validate_nombre])),
                ('clave', models.CharField(max_length=100, validators=[django.core.validators.MinLengthValidator(3)])),
                ('foto', models.ImageField(default='crypto_gym_backend/media/Clientes/default.png', upload_to='crypto_gym_backend/media/Clientes')),
                ('fechaNacimiento', models.DateField(validators=[api.validators.validate_fecha, api.validators.validate_mayordedieciochoaños])),
                ('numeroDocumento', models.CharField(max_length=50, validators=[django.core.validators.MinLengthValidator(3)])),
                ('correo', models.EmailField(max_length=254, unique=True)),
                ('numeroTelefono', models.CharField(max_length=8, validators=[api.validators.validate_numerotelefono, django.core.validators.MinLengthValidator(8)])),
                ('creado', models.DateField(default=django.utils.timezone.now)),
                ('bloqueado', models.BooleanField(default=False)),
                ('activo', models.BooleanField(default=True)),
                ('intentos', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Comida',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, validators=[django.core.validators.MinLengthValidator(3), api.validators.validate_nombre])),
                ('descripcion', models.CharField(max_length=100, validators=[django.core.validators.MinLengthValidator(3)])),
            ],
        ),
        migrations.CreateModel(
            name='Compra',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField(validators=[api.validators.validate_fecha])),
                ('valor', models.DecimalField(decimal_places=3, max_digits=10)),
                ('hora', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Cupon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NombreCodigoCupon', models.CharField(max_length=50, validators=[django.core.validators.MinLengthValidator(3), api.validators.validate_nombre])),
                ('fechaInicioCupon', models.DateTimeField()),
                ('fechaExpiracionCupon', models.DateTimeField()),
                ('descuentoCupon', models.IntegerField(validators=[django.core.validators.MinValueValidator(1)])),
            ],
            options={
                'verbose_name_plural': 'Cupones',
            },
        ),
        migrations.CreateModel(
            name='Descuento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fechaInicial', models.DateTimeField()),
                ('fechaFinal', models.DateTimeField()),
                ('codigoCupon', models.CharField(max_length=50, validators=[django.core.validators.MinLengthValidator(3), api.validators.validate_nombre])),
                ('cantidadDescuento', models.IntegerField(validators=[django.core.validators.MinValueValidator(1)])),
                ('cliente', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.cliente')),
                ('cupon', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.cupon')),
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
            name='DetallePlanilla',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sueldobruto', models.IntegerField(validators=[django.core.validators.MinValueValidator(1)])),
                ('deduccion', models.IntegerField(validators=[django.core.validators.MinValueValidator(1)])),
                ('bonificaciones', models.IntegerField(validators=[django.core.validators.MinValueValidator(1)])),
                ('detalles', models.CharField(max_length=50, validators=[django.core.validators.MinLengthValidator(3), api.validators.validate_nombre])),
            ],
        ),
        migrations.CreateModel(
            name='DocumentoEmpleado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreDocumento', models.CharField(max_length=50, validators=[django.core.validators.MinLengthValidator(3)])),
            ],
        ),
        migrations.CreateModel(
            name='Ejercicio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, validators=[django.core.validators.MinLengthValidator(3), api.validators.validate_nombre])),
                ('imagen', models.ImageField(upload_to='Ejercicios')),
                ('maquina', models.CharField(max_length=50, validators=[django.core.validators.MinLengthValidator(3), api.validators.validate_nombre])),
            ],
        ),
        migrations.CreateModel(
            name='Impuesto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, validators=[django.core.validators.MinLengthValidator(3), api.validators.validate_nombre])),
                ('valorImpuesto', models.DecimalField(decimal_places=3, max_digits=10)),
                ('fechaInicial', models.DateField(validators=[api.validators.validate_fecha])),
                ('fechaFinal', models.DateField(validators=[api.validators.validate_fecha])),
            ],
        ),
        migrations.CreateModel(
            name='LogCliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('accion', models.CharField(max_length=50, validators=[django.core.validators.MinLengthValidator(3), api.validators.validate_nombre])),
                ('informacion', models.CharField(max_length=100, validators=[django.core.validators.MinLengthValidator(3), api.validators.validate_nombre])),
                ('fecha', models.DateTimeField()),
                ('hora', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='LogEmpleado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('accion', models.CharField(max_length=50, validators=[django.core.validators.MinLengthValidator(3), api.validators.validate_nombre])),
                ('informacion', models.CharField(max_length=100, validators=[django.core.validators.MinLengthValidator(3), api.validators.validate_nombre])),
                ('fecha', models.DateTimeField()),
                ('hora', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='LogEntry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('level', models.CharField(max_length=10)),
                ('logger', models.CharField(max_length=100)),
                ('message', models.TextField()),
            ],
            options={
                'permissions': [('exportarCSV', 'Exportar CSV'), ('exportarPDF', 'Exportar PDF')],
            },
        ),
        migrations.CreateModel(
            name='LoginAdministrador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('accion', models.CharField(max_length=50, validators=[django.core.validators.MinLengthValidator(3), api.validators.validate_nombre])),
                ('informacion', models.CharField(max_length=50, validators=[django.core.validators.MinLengthValidator(3), api.validators.validate_nombre])),
                ('fecha', models.DateField(validators=[api.validators.validate_fecha])),
                ('hora', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Musculo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, validators=[django.core.validators.MinLengthValidator(3), api.validators.validate_nombre])),
            ],
        ),
        migrations.CreateModel(
            name='ParametrosFactura',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cai', models.CharField(max_length=50, validators=[django.core.validators.MinLengthValidator(3)])),
                ('fechaEmision', models.DateField()),
                ('fechaVencimiento', models.DateField()),
                ('rangoInicial', models.IntegerField(validators=[django.core.validators.MinValueValidator(0)])),
                ('rangoFinal', models.IntegerField(validators=[django.core.validators.MinValueValidator(0)])),
                ('codigoSucursal', models.IntegerField()),
                ('ultimaFactura', models.IntegerField()),
                ('activo', models.BooleanField(default=True)),
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
            name='Salon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreSalon', models.CharField(max_length=50, validators=[django.core.validators.MinLengthValidator(3), api.validators.validate_nombre])),
                ('cantidadAlumnos', models.IntegerField(validators=[django.core.validators.MinValueValidator(1)])),
            ],
            options={
                'verbose_name_plural': 'Salones',
            },
        ),
        migrations.CreateModel(
            name='TipoDocumentoCliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreDocumento', models.CharField(max_length=50, validators=[django.core.validators.MinLengthValidator(3)])),
            ],
        ),
        migrations.CreateModel(
            name='TipoGenero',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, validators=[django.core.validators.MinLengthValidator(3)])),
            ],
        ),
        migrations.CreateModel(
            name='TipoGeneroCliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreGenero', models.CharField(max_length=50, validators=[django.core.validators.MinLengthValidator(3), api.validators.validate_nombre])),
            ],
        ),
        migrations.CreateModel(
            name='TipoMembresia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreMembresia', models.CharField(max_length=50, validators=[django.core.validators.MinLengthValidator(3), api.validators.validate_nombre])),
                ('precio', models.IntegerField(validators=[django.core.validators.MinValueValidator(1)])),
                ('descripcion', models.CharField(max_length=100, validators=[django.core.validators.MinLengthValidator(3), api.validators.validate_nombre])),
            ],
        ),
        migrations.CreateModel(
            name='TipoSangreCliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreSangre', models.CharField(max_length=50, validators=[django.core.validators.MinLengthValidator(2)])),
            ],
        ),
        migrations.CreateModel(
            name='Rutina',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, validators=[django.core.validators.MinLengthValidator(3), api.validators.validate_nombre])),
                ('tipoRutina', models.CharField(max_length=100, validators=[django.core.validators.MinLengthValidator(3), api.validators.validate_nombre])),
                ('AsignacionRutina', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.asignacionrutina')),
                ('cliente', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.cliente')),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigoProducto', models.IntegerField(validators=[django.core.validators.MinValueValidator(1)])),
                ('nombre', models.CharField(max_length=50, validators=[django.core.validators.MinLengthValidator(3), api.validators.validate_nombre])),
                ('descripcion', models.CharField(max_length=100, validators=[django.core.validators.MinLengthValidator(3), api.validators.validate_nombre])),
                ('cantidad', models.IntegerField(validators=[django.core.validators.MinValueValidator(1)])),
                ('cantidadMinima', models.IntegerField(validators=[django.core.validators.MinValueValidator(1)])),
                ('imagen', models.ImageField(default='crypto_gym_backend/media/Productos/default.png', upload_to='crypto_gym_backend/media/Productos')),
                ('Categoria', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.categoria')),
                ('precioHistoricoProducto', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.preciohistoricoproducto')),
            ],
        ),
        migrations.CreateModel(
            name='PrecioHistoricoMembresia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fechaInicial', models.DateTimeField()),
                ('fechaFinal', models.DateTimeField()),
                ('precio', models.IntegerField(validators=[django.core.validators.MinValueValidator(1)])),
                ('nombreMembresias', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.tipomembresia')),
            ],
        ),
        migrations.CreateModel(
            name='Planilla',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fechaInicialPago', models.DateTimeField()),
                ('fechaFinalPago', models.DateTimeField()),
                ('DetallePlanilla', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.detalleplanilla')),
            ],
        ),
        migrations.CreateModel(
            name='Orden',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fechaOrden', models.DateField(validators=[api.validators.validate_fecha])),
                ('fechaRequerida', models.DateField(validators=[api.validators.validate_fecha])),
                ('fechaEnvio', models.DateField(validators=[api.validators.validate_fecha])),
                ('direccionEnvio', models.CharField(max_length=100, validators=[django.core.validators.MinLengthValidator(3), api.validators.validate_nombre])),
                ('cliente', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.cliente')),
            ],
        ),
        migrations.CreateModel(
            name='MusculoEjercicio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ejercicio', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.ejercicio')),
                ('musculo', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.musculo')),
            ],
        ),
        migrations.CreateModel(
            name='Membresia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fechaInicio', models.DateTimeField()),
                ('fechaFinal', models.DateTimeField()),
                ('cliente', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.cliente')),
                ('descuento', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.descuento')),
                ('tipoMembresia', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.tipomembresia')),
            ],
        ),
        migrations.CreateModel(
            name='Medidas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fechaMedida', models.DateTimeField()),
                ('fotoFrontal', models.ImageField(blank=True, null=True, upload_to='crypto_gym_backend/media/Medidas')),
                ('fotoLateral', models.ImageField(blank=True, null=True, upload_to='crypto_gym_backend/media/Medidas')),
                ('peso', models.IntegerField(validators=[django.core.validators.MinValueValidator(1)])),
                ('indiceMasaMuscular', models.DecimalField(decimal_places=3, max_digits=10)),
                ('indiceGrasaMuscular', models.DecimalField(decimal_places=3, max_digits=10)),
                ('pecho', models.DecimalField(decimal_places=3, max_digits=10)),
                ('espalda', models.DecimalField(decimal_places=3, max_digits=10)),
                ('brazo', models.DecimalField(decimal_places=3, max_digits=10)),
                ('antebrazo', models.DecimalField(decimal_places=3, max_digits=10)),
                ('cadera', models.DecimalField(decimal_places=3, max_digits=10)),
                ('cintura', models.DecimalField(decimal_places=3, max_digits=10)),
                ('pierna', models.DecimalField(decimal_places=3, max_digits=10)),
                ('pantorrilla', models.DecimalField(decimal_places=3, max_digits=10)),
                ('cliente', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.cliente')),
            ],
            options={
                'verbose_name_plural': 'Medidas',
            },
        ),
        migrations.CreateModel(
            name='Factura',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('hora', models.TimeField()),
                ('numeroFactura', models.IntegerField(validators=[django.core.validators.MinValueValidator(1)])),
                ('cliente', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.cliente')),
                ('detalleFactura', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.detallefactura')),
                ('impuesto', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.impuesto')),
                ('membresia', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.membresia')),
                ('parametrosFactura', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.parametrosfactura')),
            ],
        ),
        migrations.CreateModel(
            name='EmpleadoCargo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fechaInicio', models.DateTimeField()),
                ('fechaFinal', models.DateTimeField()),
                ('cargo', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.cargo')),
            ],
        ),
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombres', models.CharField(max_length=50, validators=[django.core.validators.MinLengthValidator(3), api.validators.validate_nombre])),
                ('apellidos', models.CharField(max_length=50, validators=[django.core.validators.MinLengthValidator(3), api.validators.validate_nombre])),
                ('clave', models.CharField(max_length=100, validators=[django.core.validators.MinLengthValidator(3)])),
                ('fechaNacimiento', models.DateField(validators=[api.validators.validate_fecha, api.validators.validate_mayordeveintiuno])),
                ('correo', models.EmailField(max_length=254, unique=True)),
                ('telefono', models.CharField(max_length=8, validators=[api.validators.validate_numerotelefono, django.core.validators.MinLengthValidator(8)])),
                ('numerodocumento', models.CharField(max_length=50, null=True, validators=[django.core.validators.MinLengthValidator(3)])),
                ('activo', models.BooleanField(default=True)),
                ('bloqueado', models.BooleanField(default=False)),
                ('creado', models.DateField(default=django.utils.timezone.now)),
                ('intentos', models.IntegerField(default=0)),
                ('rol', models.IntegerField(default=0)),
                ('documento', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.documentoempleado')),
                ('empleadoCargo', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.empleadocargo')),
                ('genero', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.tipogenero')),
                ('planilla', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.planilla')),
            ],
        ),
        migrations.CreateModel(
            name='Dieta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, validators=[django.core.validators.MinLengthValidator(3), api.validators.validate_nombre])),
                ('asignacionDieta', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.asignaciondieta')),
                ('cliente', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.cliente')),
            ],
        ),
        migrations.CreateModel(
            name='Devolucion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fechaDevolucion', models.DateField(validators=[api.validators.validate_fecha])),
                ('cantidad', models.IntegerField(validators=[django.core.validators.MinValueValidator(1)])),
                ('nombreProducto', models.CharField(max_length=50, validators=[django.core.validators.MinLengthValidator(3), api.validators.validate_nombre])),
                ('razonDevolucion', models.CharField(max_length=50, validators=[django.core.validators.MinLengthValidator(3), api.validators.validate_nombre])),
                ('detalleFactura', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.detallefactura')),
            ],
        ),
        migrations.CreateModel(
            name='DetallesOrden',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('precio', models.DecimalField(decimal_places=3, max_digits=10)),
                ('cantidad', models.IntegerField(validators=[django.core.validators.MinValueValidator(1)])),
                ('orden', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.orden')),
                ('producto', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.producto')),
            ],
        ),
        migrations.AddField(
            model_name='detallefactura',
            name='producto',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.producto'),
        ),
        migrations.AddField(
            model_name='cliente',
            name='TipoDocumento',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.tipodocumentocliente'),
        ),
        migrations.AddField(
            model_name='cliente',
            name='genero',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.tipogenerocliente'),
        ),
        migrations.AddField(
            model_name='cliente',
            name='tipoSangre',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.tiposangrecliente'),
        ),
        migrations.AddField(
            model_name='asignacionrutina',
            name='MusculoEjercicio',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.musculoejercicio'),
        ),
        migrations.AddField(
            model_name='asignaciondieta',
            name='comida',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.comida'),
        ),
        migrations.CreateModel(
            name='AsignacionClase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('horario', models.DateTimeField()),
                ('fecha', models.DateField(validators=[api.validators.validate_fecha])),
                ('cliente', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.cliente')),
                ('empleado', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.empleado')),
                ('nombreClase', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.clasegrupal')),
                ('salon', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.salon')),
            ],
        ),
    ]
