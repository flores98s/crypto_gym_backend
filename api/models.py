from django.core.validators import MinLengthValidator,MinValueValidator, MaxLengthValidator
from django.db import models
from django.utils import timezone
from datetime import date
from django.core.exceptions import ValidationError
from .validators import *

# Modelo TipoMembresia.
class TipoMembresia(models.Model):
    nombreMembresia = models.CharField(validators=[MinLengthValidator(3),validate_nombre],  max_length=50)
    precio = models.IntegerField(validators=[MinValueValidator(1)])
    descripcion = models.CharField(validators=[MinLengthValidator(3),validate_nombre], max_length=100)

    def __str__(self):
        return self.nombreMembresia

# Modelo PrecioHistoricoMembresia.
class PrecioHistoricoMembresia(models.Model):
    nombreMembresias = models.ForeignKey(TipoMembresia, on_delete=models.SET_NULL, null=True, blank=True)
    fechaInicial = models.DateTimeField()
    fechaFinal = models.DateTimeField()
    precio = models.IntegerField(validators=[MinValueValidator(1)])

    def __str__(self):
        return self.nombreMembresias


# Modelo Membresia.
class Membresia(models.Model):
    tipoMembresia = models.ForeignKey(TipoMembresia, on_delete=models.SET_NULL, null=True, blank=True)
    fechaInicio = models.DateTimeField()
    fechaFinal = models.DateTimeField()
    

    def __str__(self):
        return self.tipoMembresia
#Modelo Descuento.
#Modelo Cupones.
class Cupon(models.Model):
    NombreCodigoCupon = models.CharField(validators=[MinLengthValidator(3),validate_nombre], max_length=50)
    fechaInicioCupon = models.DateTimeField()
    fechaExpiracionCupon = models.DateTimeField()
    descuentoCupon = models.IntegerField(validators=[MinValueValidator(1)])

    class Meta:
        verbose_name_plural = "Cupones"

    def __str__(self):
        return self.NombreCodigoCupon

# Modelo TipoGeneroCliente.
class TipoGeneroCliente(models.Model):
    nombreGenero = models.CharField(validators=[MinLengthValidator(3),validate_nombre], max_length=50)

    def __str__(self):
        return self.nombreGenero

# Modelo TipoDocumentoCliente.
class TipoDocumentoCliente(models.Model):
    nombreDocumento = models.CharField(validators=[MinLengthValidator(3)], max_length=50)
    
    def __str__(self):
        return self.nombreDocumento

# Modelo TipoSangreCliente.
class TipoSangreCliente(models.Model):
    nombreSangre = models.CharField(validators=[MinLengthValidator(3),validate_nombre], max_length=50)
   
    def __str__(self):
        return self.nombreSangre

# Modelo Cliente.
class Cliente(models.Model):
    nombres = models.CharField(validators=[MinLengthValidator(2),validate_nombre], max_length=50)
    apellidos = models.CharField(validators=[MinLengthValidator(2),validate_nombre], max_length=50)
    clave = models.CharField(validators=[MinLengthValidator(3)], max_length=100)
    foto = models.CharField(validators=[MinLengthValidator(3),validate_nombre], max_length=50)
    fechaNacimiento = models.DateField(validators=[validate_fecha, validate_mayordedieciochoaños])
    TipoDocumento = models.ForeignKey(TipoDocumentoCliente, on_delete=models.SET_NULL, null=True, blank=True)
    numeroDocumento = models.CharField(validators=[MinLengthValidator(3)], max_length=50)
    correo = models.EmailField(unique=True)
    numeroTelefono = models.CharField(validators=[validate_numerotelefono, MinLengthValidator(8)], max_length=(8))
    genero = models.ForeignKey(TipoGeneroCliente, on_delete=models.SET_NULL, null=True, blank=True)
    tipoSangre = models.ForeignKey(TipoSangreCliente, on_delete=models.SET_NULL, null=True, blank=True)
    creado = models.DateField(default=timezone.now)
    bloqueado = models.BooleanField(default=False)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return self.nombres+" "+self.apellidos


class Descuento(models.Model):
    membresia = models.ForeignKey(Membresia, on_delete=models.SET_NULL, null=True, blank=True)
    Cliente = models.ForeignKey(Cliente, on_delete=models.SET_NULL, null=True, blank=True)
    cupon = models.ForeignKey(Cupon, on_delete=models.SET_NULL, null=True, blank=True)
    fechaInicial = models.DateTimeField()
    fechaFinal = models.DateTimeField()
    codigoCupon = models.CharField(validators=[MinLengthValidator(3),validate_nombre], max_length=50)
    cantidadDescuento = models.IntegerField(validators=[MinValueValidator(1)])

    def __str__(self):
        return self.membresia

# Modelo Medidas.
class Medidas(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.SET_NULL, null=True, blank=True)
    fechaMedida = models.DateTimeField()
    fotoFrontal = models.CharField(validators=[MinLengthValidator(3),validate_nombre], max_length=50)
    fotoLateral = models.CharField(validators=[MinLengthValidator(3),validate_nombre], max_length=50)
    peso = models.IntegerField(validators=[MinValueValidator(1)])
    indiceMasaMuscular = models.DecimalField(decimal_places=3,max_digits=10)
    indiceGrasaMuscular = models.DecimalField(decimal_places=3,max_digits=10)
    pecho = models.DecimalField(decimal_places=3,max_digits=10)
    espalda = models.DecimalField(decimal_places=3,max_digits=10)
    brazo = models.DecimalField(decimal_places=3,max_digits=10)
    antebrazo = models.DecimalField(decimal_places=3,max_digits=10)
    cadera = models.DecimalField(decimal_places=3,max_digits=10)
    cintura = models.DecimalField(decimal_places=3,max_digits=10)
    pierna = models.DecimalField(decimal_places=3,max_digits=10)
    pantorrilla= models.DecimalField(decimal_places=3,max_digits=10)
   
    class Meta:
        verbose_name_plural = "Medidas"

    def __str__(self):
        return self.cliente


#Modelo LogCliente.
class LogCliente(models.Model):
    accion = models.CharField(validators=[MinLengthValidator(3),validate_nombre], max_length=50)
    informacion = models.CharField(validators=[MinLengthValidator(3),validate_nombre], max_length=100)
    fecha = models.DateTimeField()
    hora = models.TimeField()
    
# Modelo TipoGenero.
class TipoGenero(models.Model):
    nombre = models.CharField(validators=[MinLengthValidator(3)], max_length=50)

    def __str__(self):
        return self.nombre

#Modelo TipoDocumento.
class DocumentoEmpleado(models.Model):
    nombreDocumento = models.CharField(validators=[MinLengthValidator(3)], max_length=50)

    def __str__(self):
        return self.nombreDocumento

# Modelo Empleado.
class Empleado(models.Model):
    nombres = models.CharField(validators=[MinLengthValidator(3),validate_nombre], max_length=50)
    apellidos = models.CharField(validators=[MinLengthValidator(3),validate_nombre], max_length=50)
    clave = models.CharField(validators=[MinLengthValidator(3)], max_length=100)
    fechaNacimiento = models.DateField(validators=[validate_fecha, validate_mayordeveintiuno])
    correo = models.EmailField(unique=True)
    telefono = models.CharField(validators=[validate_numerotelefono, MinLengthValidator(8)], max_length=(8))
    genero = models.ForeignKey(TipoGenero, on_delete=models.SET_NULL, null=True, blank=True)
    documento = models.ForeignKey(DocumentoEmpleado, on_delete=models.SET_NULL, null=True, blank=True)
    numerodocumento = models.CharField(validators=[MinLengthValidator(3)], max_length=50, null=True)

    def __str__(self):
        return self.nombres+" "+self.apellidos

# Modelo DetallePlanilla.
class DetallePlanilla(models.Model):
    sueldobruto = models.IntegerField(validators=[MinValueValidator(1)])
    deduccion = models.IntegerField(validators=[MinValueValidator(1)])
    bonificaciones = models.IntegerField(validators=[MinValueValidator(1)])
    detalles = models.CharField(validators=[MinLengthValidator(3),validate_nombre], max_length=50)

# Modelo Planilla.
class Planilla(models.Model):
    empleado = models.ForeignKey(Empleado, on_delete=models.SET_NULL, null=True, blank=True)
    DetallePlanilla = models.ForeignKey(DetallePlanilla, on_delete=models.SET_NULL, null=True, blank=True)
    fechaInicialPago = models.DateTimeField()
    fechaFinalPago = models.DateTimeField()

    def __str__(self):
        return self.empleado

# ------------------- MODELOS DE EMPLEADO ------------------- #

#Modelo Cargo
class Cargo(models.Model):
    nombreCargo = models.CharField(validators=[MinLengthValidator(3),validate_nombre], max_length=50)
    salario = models.DecimalField(decimal_places=3,max_digits=10)

    def __str__(self):
        return self.nombreCargo

# Modelo Salon 
class Salon(models.Model):
    nombreSalon = models.CharField(validators=[MinLengthValidator(3),validate_nombre], max_length=50)
    cantidadAlumnos = models.IntegerField(validators=[MinValueValidator(1)])

    class Meta:
        verbose_name_plural = "Salones"

    def __str__(self):
        return self.nombreSalon

# Modelo Empleados Cargos
class EmpleadoCargo(models.Model):
    empleado = models.ForeignKey(Empleado, on_delete=models.SET_NULL, null=True, blank=True)
    cargo = models.ForeignKey(Cargo, on_delete=models.SET_NULL, null=True, blank=True)
    fechaInicio = models.DateTimeField()
    fechaFinal = models.DateTimeField()

    def __str__(self):
        return self.empleado

# Modelo Clase Grupal
class ClaseGrupal(models.Model):
    
    nombreClase = models.CharField(validators=[MinLengthValidator(3),validate_nombre], max_length=50)
    cantidadAlumnos = models.IntegerField(validators=[MinValueValidator(1)])
    class Meta :
        verbose_name_plural = "Clases Grupales"

    def __str__(self):
        return self.nombreClase

# Modelo Asignacion Clase
class AsignacionClase(models.Model):
    empleado = models.ForeignKey(Empleado, on_delete=models.SET_NULL, null=True, blank=True)
    nombreClase = models.ForeignKey(ClaseGrupal, on_delete=models.SET_NULL, null=True, blank=True)
    salon = models.ForeignKey(Salon, on_delete=models.SET_NULL, null=True, blank=True)
    horario = models.DateTimeField()
    fecha = models.DateField(validators=[validate_fecha])

    def __str__(self):
        return self.nombreClase

#Modelo LogEmpleado
class LogEmpleado(models.Model):
    accion = models.CharField(validators=[MinLengthValidator(3),validate_nombre], max_length=50)
    informacion = models.CharField(validators=[MinLengthValidator(3),validate_nombre], max_length=100)
    fecha = models.DateTimeField()
    hora = models.TimeField()

class Comida(models.Model):
    nombre = models.CharField(validators=[MinLengthValidator(3),validate_nombre], max_length=50)
    descripcion = models.CharField(validators=[MinLengthValidator(3),validate_nombre], max_length=100)

    def __str__(self):
        return self.nombre

class AsignacionDieta(models.Model):
    comida = models.ForeignKey(Comida, on_delete=models.SET_NULL, null=True, blank=True)
    fecha = models.DateField(validators=[validate_fecha])
    hora = models.TimeField()

    def __str__(self):
        return self.comida

class Dieta(models.Model):
    empleado = models.ForeignKey(Empleado, on_delete=models.SET_NULL, null=True, blank=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.SET_NULL, null=True, blank=True)
    asignacionDieta = models.ForeignKey(AsignacionDieta, on_delete=models.SET_NULL, null=True, blank=True)
    nombre = models.CharField(validators=[MinLengthValidator(3),validate_nombre], max_length=50)

    def __str__(self):
        return self.asignacionDieta

class Ejercicio(models.Model):
    nombre = models.CharField(validators=[MinLengthValidator(3),validate_nombre], max_length=50)
    imagen = models.ImageField(upload_to='Ejercicios')
    maquina = models.CharField(validators=[MinLengthValidator(3),validate_nombre], max_length=50)

    def __str__(self):
        return self.nombre

class Musculo(models.Model):
    nombre = models.CharField(validators=[MinLengthValidator(3),validate_nombre], max_length=50)

    def __str__(self):
        return self.nombre

class MusculoEjercicio(models.Model):   
    musculo = models.ForeignKey(Musculo, on_delete=models.SET_NULL, null=True, blank=True)
    ejercicio = models.ForeignKey(Ejercicio, on_delete=models.SET_NULL, null=True, blank=True)

class AsignacionRutina(models.Model):
    MusculoEjercicio = models.ForeignKey(MusculoEjercicio, on_delete=models.SET_NULL, null=True, blank=True)
    series = models.CharField(validators=[MinLengthValidator(3),validate_nombre], max_length=50)
    repeticiones = models.CharField(validators=[MinLengthValidator(3),validate_nombre], max_length=50)
    descanso = models.CharField(validators=[MinLengthValidator(3),validate_nombre], max_length=50)
    capacidad = models.CharField(validators=[MinLengthValidator(3),validate_nombre], max_length=50)

    def __str__(self):
        return self.MusculoEjercicio

    class Meta:
        verbose_name_plural = "Asignaciones Rutinas"

class Rutina(models.Model):
    empleado = models.ForeignKey(Empleado, on_delete=models.SET_NULL, null=True, blank=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.SET_NULL, null=True, blank=True)
    AsignacionRutina = models.ForeignKey(AsignacionRutina, on_delete=models.SET_NULL, null=True, blank=True)
    nombre = models.CharField(validators=[MinLengthValidator(3),validate_nombre], max_length=50)
    tipoRutina = models.CharField(validators=[MinLengthValidator(3),validate_nombre], max_length=100)

    def __str__(self):
        return self.cliente
#-------------------------------------------------------------------------------------------------------------------------------
#Modelo Producto
class Producto(models.Model):
   codigoProducto = models.IntegerField(validators=[MinValueValidator(1)])
   nombre = models.CharField(validators=[MinLengthValidator(3),validate_nombre], max_length=50)
   descripcion = models.CharField(validators=[MinLengthValidator(3),validate_nombre], max_length=100)
   cantidad = models.IntegerField(validators=[MinValueValidator(1)])
   cantidadMinima = models.IntegerField(validators=[MinValueValidator(1)])

   def __str__(self):
       return self.nombre

#Modelo Detalle Factura
class DetalleFactura(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.SET_NULL, null=True, blank=True)
    cantidad = models.IntegerField(validators=[MinValueValidator(1)])
    precio = models.DecimalField(decimal_places=3,max_digits=10)
    subtotal = models.DecimalField(decimal_places=3,max_digits=10)
    descuento = models.DecimalField(decimal_places=3,max_digits=10)
    total = models.DecimalField(decimal_places=3,max_digits=10)

    def __str__(self):
        return self.producto

#Modelo Parametros Factura
class ParametrosFactura(models.Model):
    cai = models.CharField(validators=[MinLengthValidator(3),validate_nombre], max_length=50)
    fechaEmision = models.DateField(validators=[validate_fecha])
    fechaVencimiento = models.DateField(validators=[validate_fecha])
    rangoInicial = models.IntegerField(validators=[MinValueValidator(1)])
    rangoFinal = models.IntegerField(validators=[MinValueValidator(1)])
    codigoSucursal = models.IntegerField(validators=[MinValueValidator(1)])
    ultimaFactura = models.IntegerField(validators=[MinValueValidator(1)])

    def __str__(self):
        return self.cai

#Modelo Impuesto
class Impuesto(models.Model):
    nombre = models.CharField(validators=[MinLengthValidator(3),validate_nombre], max_length=50)
    valorImpuesto = models.DecimalField(decimal_places=3,max_digits=10)
    fechaInicial = models.DateField(validators=[validate_fecha])
    fechaFinal = models.DateField(validators=[validate_fecha])

    def __str__(self):
        return self.nombre

#Modelo Factura
class Factura(models.Model):
    detalleFactura = models.ForeignKey(DetalleFactura, on_delete=models.SET_NULL, null=True, blank=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.SET_NULL, null=True, blank=True)
    parametrosFactura = models.ForeignKey(ParametrosFactura, on_delete=models.SET_NULL, null=True, blank=True)
    impuesto = models.ForeignKey(Impuesto, on_delete=models.SET_NULL, null=True, blank=True)
    membresia = models.ForeignKey(Membresia, on_delete=models.SET_NULL, null=True, blank=True)
    fecha = models.DateField(validators=[validate_fecha])
    hora = models.TimeField()
    numeroFactura = models.IntegerField(validators=[MinValueValidator(1)])

    def __str__(self):
        return self.detalleFactura

#Modelo Devolucion
class Devolucion(models.Model):
    detalleFactura = models.ForeignKey(DetalleFactura, on_delete=models.SET_NULL, null=True, blank=True)
    fechaDevolucion = models.DateField(validators=[validate_fecha])
    cantidad = models.IntegerField(validators=[MinValueValidator(1)])
    nombreProducto = models.CharField(validators=[MinLengthValidator(3),validate_nombre], max_length=50)
    razonDevolucion = models.CharField(validators=[MinLengthValidator(3),validate_nombre], max_length=50)

    def __str__(self):
        return self.detalleFactura
    
#Modelo Orden
class Orden(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.SET_NULL, null=True, blank=True)
    fechaOrden = models.DateField(validators=[validate_fecha])
    fechaRequerida = models.DateField(validators=[validate_fecha])
    fechaEnvio = models.DateField(validators=[validate_fecha])
    direccionEnvio = models.CharField(validators=[MinLengthValidator(3),validate_nombre], max_length=100)

    def __str__(self):
        return self.cliente

#Modelo Detalles Orden
class DetallesOrden(models.Model):
    orden = models.ForeignKey(Orden, on_delete=models.SET_NULL, null=True, blank=True)
    producto = models.ForeignKey(Producto, on_delete=models.SET_NULL, null=True, blank=True)
    precio = models.DecimalField(decimal_places=3,max_digits=10)
    cantidad = models.IntegerField(validators=[MinValueValidator(1)])

    def __str__(self):
        return self.orden

#Modelo Categoria
class Categoria(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.SET_NULL, null=True, blank=True)
    nombre = models.CharField(validators=[MinLengthValidator(3),validate_nombre], max_length=50)

    def __str__(self):
        return self.nombre

#Modelo Precio Historico Producto
class PrecioHistoricoProducto(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.SET_NULL, null=True, blank=True)
    fechaInicial = models.DateField(validators=[validate_fecha])
    fechaFinal = models.DateField(validators=[validate_fecha])
    precio = models.DecimalField(decimal_places=3,max_digits=10)
    
    def __str__(self):
        return self.producto

#Modelo Compra
class Compra(models.Model):
    fecha = models.DateField(validators=[validate_fecha])
    valor = models.DecimalField(decimal_places=3,max_digits=10)
    hora = models.TimeField()

#Modelo Administrador
class Administrador(models.Model):
    nombre = models.CharField(validators=[MinLengthValidator(3),validate_nombre], max_length=50)
    apellido = models.CharField(validators=[MinLengthValidator(3),validate_nombre], max_length=50)
    correo = models.EmailField()
    telefono = models.CharField(validators=[MinLengthValidator(3),validate_nombre], max_length=50)

#Modelo Login Administrador
class LoginAdministrador(models.Model):
    accion = models.CharField(validators=[MinLengthValidator(3),validate_nombre], max_length=50)
    informacion = models.CharField(validators=[MinLengthValidator(3),validate_nombre], max_length=50)
    fecha = models.DateField(validators=[validate_fecha])
    hora = models.TimeField()

