from django.core.validators import MinLengthValidator,MinValueValidator
from django.db import models
from django.utils import timezone
from datetime import date
from django.core.exceptions import ValidationError

# Modelo TipoMembresia.
class TipoMembresia(models.Model):
    nombreMembresia = models.CharField(validators=[MinLengthValidator(3)],  max_length=50)
    precio = models.IntegerField(validators=[MinValueValidator(1)])
    descripcion = models.CharField(validators=[MinLengthValidator(3)], max_length=100)

    def __str__(self):
        return self.nombreMembresia

# Modelo PrecioHistoricoMembresia.
class PrecioHistoricoMembresia(models.Model):
    fechaInicial = models.DateTimeField()
    fechaFinal = models.DateTimeField()
    precio = models.IntegerField(validators=[MinValueValidator(1)])
    nombreMembresias = models.ForeignKey(TipoMembresia, on_delete=models.SET_NULL, null=True, blank=True)

# Modelo Membresia.
class Membresia(models.Model):
    fechaInicio = models.DateTimeField()
    fechaFinal = models.DateTimeField()
    tipoMembresia = models.ForeignKey(TipoMembresia, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.tipoMembresia

#Modelo Descuento.
class Descuento(models.Model):
    fechaInicial = models.DateTimeField()
    fechaFinal = models.DateTimeField()
    codigoCupon = models.CharField(validators=[MinLengthValidator(3)], max_length=50)
    cantidadDescuento = models.IntegerField(validators=[MinValueValidator(1)])

#Modelo Cupones.
class Cupon(models.Model):
    NombreCodigoCupon = models.CharField(validators=[MinLengthValidator(3)], max_length=50)
    fechaInicioCupon = models.DateTimeField()
    fechaExpiracionCupon = models.DateTimeField()
    descuentoCupon = models.IntegerField(validators=[MinValueValidator(1)])

    class Meta:
        verbose_name_plural = "Cupones"

    def __str__(self):
        return self.NombreCodigoCupon


# Modelo TipoGeneroCliente.
class TipoGeneroCliente(models.Model):
    nombreGenero = models.CharField(validators=[MinLengthValidator(3)], max_length=50)

    def __str__(self):
        return self.nombreGenero

# Modelo TipoDocumentoCliente.
class TipoDocumentoCliente(models.Model):
    nombreDocumento = models.CharField(validators=[MinLengthValidator(3)], max_length=50)
    
    def __str__(self):
        return self.nombreDocumento

# Modelo TipoSangreCliente.
class TipoSangreCliente(models.Model):
    nombreSangre = models.CharField(validators=[MinLengthValidator(3)], max_length=50)
   
    def __str__(self):
        return self.nombreSangre

# Modelo Cliente.
class Cliente(models.Model):
    nombres = models.CharField(validators=[MinLengthValidator(2)], max_length=50)
    apellidos = models.CharField(validators=[MinLengthValidator(2)], max_length=50)
    clave = models.CharField(validators=[MinLengthValidator(3)], max_length=50)
    foto = models.CharField(validators=[MinLengthValidator(3)], max_length=50)
    fechaNacimiento = models.DateField()
    TipoDocumento = models.ForeignKey(TipoDocumentoCliente, on_delete=models.SET_NULL, null=True, blank=True)
    numeroDocumento = models.CharField(validators=[MinLengthValidator(3)], max_length=50)
    correo = models.EmailField()
    numeroTelefono = models.IntegerField(validators=[MinValueValidator(1)])
    genero = models.ForeignKey(TipoGeneroCliente, on_delete=models.SET_NULL, null=True, blank=True)
    tipoSangre = models.ForeignKey(TipoSangreCliente, on_delete=models.SET_NULL, null=True, blank=True)
    creado = models.DateField(default=timezone.now)

    def __str__(self):
        return self.nombres+" "+self.apellidos

#Modelo LogCliente.
class LogCliente(models.Model):
    accion = models.CharField(validators=[MinLengthValidator(3)], max_length=50)
    informacion = models.CharField(validators=[MinLengthValidator(3)], max_length=100)
    fecha = models.DateTimeField()
    hora = models.TimeField()
    
# Modelo Medidas.
class Medidas(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.SET_NULL, null=True, blank=True)
    fechaMedida = models.DateTimeField()
    fotoFrontal = models.CharField(validators=[MinLengthValidator(3)], max_length=50)
    fotoLateral = models.CharField(validators=[MinLengthValidator(3)], max_length=50)
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

# Modelo Empleado.
class Empleado(models.Model):
    nombres = models.CharField(validators=[MinLengthValidator(3)], max_length=50)
    apellidos = models.CharField(validators=[MinLengthValidator(3)], max_length=50)
    clave = models.CharField(validators=[MinLengthValidator(3)], max_length=50)
    fechaNacimiento = models.DateField()
    correo = models.EmailField()
    telefono = models.IntegerField(validators=[MinValueValidator(1)])
    genero = models.IntegerField(validators=[MinValueValidator(1)])
    documento = models.CharField(validators=[MinLengthValidator(3)], max_length=50)
    numerodocumento = models.CharField(validators=[MinLengthValidator(3)], max_length=50, null=True)

    def __str__(self):
        return self.nombres+" "+self.apellidos

    def clean(self) -> None:
        #Dias en 21 años
        veintiunAñosEnDias = 365.2425 * 21
        hoy = date.today() 
        diferenciaDias =  hoy - self.fechaNacimiento
        if self.fechaNacimiento >= hoy:
            raise ValidationError("La fecha de nacimiento no puede ser mayor o igual a la fecha de hoy")
        
        if diferenciaDias.days < veintiunAñosEnDias:
            raise ValidationError("El empleado no puede tener menos de 21 años")
        
# Modelo TipoGenero.
class TipoGenero(models.Model):
    nombre = models.CharField(validators=[MinLengthValidator(3)], max_length=50)

    def __str__(self):
        return self.nombre

# Modelo Planilla.
class Planilla(models.Model):
    fechaInicialPago = models.DateTimeField()
    fechaFinalPago = models.DateTimeField()

# Modelo DetallePlanilla.
class DetallePlanilla(models.Model):
    sueldobruto = models.IntegerField(validators=[MinValueValidator(1)])
    deduccion = models.IntegerField(validators=[MinValueValidator(1)])
    bonificaciones = models.IntegerField(validators=[MinValueValidator(1)])
    detalles = models.CharField(validators=[MinLengthValidator(3)], max_length=50)

# ------------------- MODELOS DE EMPLEADO ------------------- #

#Modelo TipoDocumento.
class DocumentoEmpleado(models.Model):
    nombreDocumento = models.CharField(validators=[MinLengthValidator(3)], max_length=50)

    def __str__(self):
        return self.nombreDocumento

# Modelo Empleados Cargos
class EmpleadoCargo(models.Model):
    fechaInicio = models.DateTimeField()
    fechaFinal = models.DateTimeField()

#Modelo Cargo
class Cargo(models.Model):
    nombreCargo = models.CharField(validators=[MinLengthValidator(3)], max_length=50)
    salario = models.DecimalField(decimal_places=3,max_digits=10)

    def __str__(self):
        return self.nombreCargo

# Modelo Asignacion Clase
class AsignacionClase(models.Model):
    horario = models.DateTimeField()
    fecha = models.DateField()

# Modelo Clase Grupal
class ClaseGrupal(models.Model):
    nombreClase = models.CharField(validators=[MinLengthValidator(3)], max_length=50)
    cantidadAlumnos = models.IntegerField(validators=[MinValueValidator(1)])
    class Meta :
        verbose_name_plural = "Clases Grupales"

    def __str__(self):
        return self.nombreClase

# Modelo Salon 
class Salon(models.Model):
    nombreSalon = models.CharField(validators=[MinLengthValidator(3)], max_length=50)
    cantidadAlumnos = models.IntegerField(validators=[MinValueValidator(1)])

    class Meta:
        verbose_name_plural = "Salones"

    def __str__(self):
        return self.nombreSalon

#Modelo LogEmpleado
class LogEmpleado(models.Model):
    accion = models.CharField(validators=[MinLengthValidator(3)], max_length=50)
    informacion = models.CharField(validators=[MinLengthValidator(3)], max_length=100)
    fecha = models.DateTimeField()
    hora = models.TimeField()

""" Modelo de tablas agregadas por el equipo de desarrollo """

class Dieta(models.Model):
    nombre = models.CharField(validators=[MinLengthValidator(3)], max_length=50)

    def __str__(self):
        return self.nombre

class AsignacionDieta(models.Model):
    fecha = models.DateField()
    hora = models.TimeField()

class Comida(models.Model):
    nombre = models.CharField(validators=[MinLengthValidator(3)], max_length=50)
    descripcion = models.CharField(validators=[MinLengthValidator(3)], max_length=100)

    def __str__(self):
        return self.nombre

class Rutina(models.Model):
    nombre = models.CharField(validators=[MinLengthValidator(3)], max_length=50)
    tipoRutina = models.CharField(validators=[MinLengthValidator(3)], max_length=100)

    def __str__(self):
        return self.nombre

class AsignacionRutina(models.Model):
    series = models.CharField(validators=[MinLengthValidator(3)], max_length=50)
    repeticiones = models.CharField(validators=[MinLengthValidator(3)], max_length=50)
    descanso = models.CharField(validators=[MinLengthValidator(3)], max_length=50)
    capacidad = models.CharField(validators=[MinLengthValidator(3)], max_length=50)

class Ejercicio(models.Model):
    nombre = models.CharField(validators=[MinLengthValidator(3)], max_length=50)
    imagen = models.ImageField(upload_to='Ejercicios')
    maquina = models.CharField(validators=[MinLengthValidator(3)], max_length=50)

    def __str__(self):
        return self.nombre

class Musculo(models.Model):
    nombre = models.CharField(validators=[MinLengthValidator(3)], max_length=50)

    def __str__(self):
        return self.nombre

#Modelo Factura
class Factura(models.Model):
    fecha = models.DateField()
    hora = models.TimeField()
    numeroFactura = models.IntegerField(validators=[MinValueValidator(1)])

#Modelo Parametros Factura
class ParametrosFactura(models.Model):
    cai = models.CharField(validators=[MinLengthValidator(3)], max_length=50)
    fechaEmision = models.DateField()
    fechaVencimiento = models.DateField()
    rangoInicial = models.IntegerField(validators=[MinValueValidator(1)])
    rangoFinal = models.IntegerField(validators=[MinValueValidator(1)])
    codigoSucursal = models.IntegerField(validators=[MinValueValidator(1)])
    ultimaFactura = models.IntegerField(validators=[MinValueValidator(1)])

#Modelo Impuesto
class Impuesto(models.Model):
    nombre = models.CharField(validators=[MinLengthValidator(3)], max_length=50)
    valorImpuesto = models.DecimalField(decimal_places=3,max_digits=10)
    fechaInicial = models.DateField()
    fechaFinal = models.DateField()

#Modelo Detalle Factura
class DetalleFactura(models.Model):
    cantidad = models.IntegerField(validators=[MinValueValidator(1)])
    precio = models.DecimalField(decimal_places=3,max_digits=10)
    subtotal = models.DecimalField(decimal_places=3,max_digits=10)
    descuento = models.DecimalField(decimal_places=3,max_digits=10)
    total = models.DecimalField(decimal_places=3,max_digits=10)

#Modelo Devolucion
class Devolucion(models.Model):
    fechaDevolucion = models.DateField()
    cantidad = models.IntegerField(validators=[MinValueValidator(1)])
    nombreProducto = models.CharField(validators=[MinLengthValidator(3)], max_length=50)
    razonDevolucion = models.CharField(validators=[MinLengthValidator(3)], max_length=50)

#Modelo Producto
class Producto(models.Model):
   codigoProducto = models.IntegerField(validators=[MinValueValidator(1)])
   nombre = models.CharField(validators=[MinLengthValidator(3)], max_length=50)
   descripcion = models.CharField(validators=[MinLengthValidator(3)], max_length=100)
   cantidad = models.IntegerField(validators=[MinValueValidator(1)])
   cantidadMinima = models.IntegerField(validators=[MinValueValidator(1)])

#Modelo Detalles Orden
class DetallesOrden(models.Model):
    precio = models.DecimalField(decimal_places=3,max_digits=10)
    cantidad = models.IntegerField(validators=[MinValueValidator(1)])
    
#Modelo Orden
class Orden(models.Model):
    fechaOrden = models.DateField()
    fechaRequerida = models.DateField()
    fechaEnvio = models.DateField()
    direccionEnvio = models.CharField(validators=[MinLengthValidator(3)], max_length=100)

#Modelo Categoria
class Categoria(models.Model):
    nombre = models.CharField(validators=[MinLengthValidator(3)], max_length=50)

#Modelo Precio Historico Producto
class PrecioHistoricoProducto(models.Model):
    fechaInicial = models.DateField()
    fechaFinal = models.DateField()
    precio = models.DecimalField(decimal_places=3,max_digits=10)
    
#Modelo Compra
class Compra(models.Model):
    fecha = models.DateField()
    valor = models.DecimalField(decimal_places=3,max_digits=10)
    hora = models.TimeField()

#Modelo Administrador
class Administrador(models.Model):
    nombre = models.CharField(validators=[MinLengthValidator(3)], max_length=50)
    apellido = models.CharField(validators=[MinLengthValidator(3)], max_length=50)
    correo = models.EmailField()
    telefono = models.CharField(validators=[MinLengthValidator(3)], max_length=50)

#Modelo Login Administrador
class LoginAdministrador(models.Model):
    accion = models.CharField(validators=[MinLengthValidator(3)], max_length=50)
    informacion = models.CharField(validators=[MinLengthValidator(3)], max_length=50)
    fecha = models.DateField()
    hora = models.TimeField()

