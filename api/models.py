from django.db import models
from django.utils import timezone
from datetime import date
from django.core.exceptions import ValidationError

# Modelo TipoMembresia.
class TipoMembresia(models.Model):
    nombreMembresia = models.CharField(max_length=50)
    precio = models.IntegerField()
    descripcion = models.CharField(max_length=100)

    def __str__(self):
        return self.nombreMembresia

# Modelo PrecioHistoricoMembresia.
class PrecioHistoricoMembresia(models.Model):
    fechaInicial = models.DateTimeField()
    fechaFinal = models.DateTimeField()
    precio = models.IntegerField()
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
    codigoCupon = models.CharField(max_length=50)
    cantidadDescuento = models.IntegerField()

#Modelo Cupones.
class Cupon(models.Model):
    NombreCodigoCupon = models.CharField(max_length=50)
    fechaInicioCupon = models.DateTimeField()
    fechaExpiracionCupon = models.DateTimeField()
    descuentoCupon = models.IntegerField()

    class Meta:
        verbose_name_plural = "Cupones"

    def __str__(self):
        return self.NombreCodigoCupon


# Modelo TipoGeneroCliente.
class TipoGeneroCliente(models.Model):
    nombreGenero = models.CharField(max_length=50)

    def __str__(self):
        return self.nombreGenero

# Modelo TipoDocumentoCliente.
class TipoDocumentoCliente(models.Model):
    nombreDocumento = models.CharField(max_length=50)
    
    def __str__(self):
        return self.nombreDocumento

# Modelo TipoSangreCliente.
class TipoSangreCliente(models.Model):
    nombreSangre = models.CharField(max_length=50)
   
    def __str__(self):
        return self.nombreSangre

# Modelo Cliente.
class Cliente(models.Model):
    nombres = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    clave = models.CharField(max_length=50)
    foto = models.CharField(max_length=50)
    fechaNacimiento = models.DateField()
    TipoDocumento = models.ForeignKey(TipoDocumentoCliente, on_delete=models.SET_NULL, null=True, blank=True)
    numeroDocumento = models.CharField(max_length=50)
    correo = models.EmailField()
    numeroTelefono = models.IntegerField()
    genero = models.ForeignKey(TipoGeneroCliente, on_delete=models.SET_NULL, null=True, blank=True)
    tipoSangre = models.ForeignKey(TipoSangreCliente, on_delete=models.SET_NULL, null=True, blank=True)
    creado = models.DateField(default=timezone.now)

    def __str__(self):
        return self.nombres+" "+self.apellidos

#Modelo LogCliente.
class LogCliente(models.Model):
    accion = models.CharField(max_length=50)
    informacion = models.CharField(max_length=100)
    fecha = models.DateTimeField()
    hora = models.TimeField()
    
# Modelo Medidas.
class Medidas(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.SET_NULL, null=True, blank=True)
    fechaMedida = models.DateTimeField()
    fotoFrontal = models.CharField(max_length=50)
    fotoLateral = models.CharField(max_length=50)
    peso = models.IntegerField()
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
    nombres = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    clave = models.CharField(max_length=50)
    fechaNacimiento = models.DateField()
    correo = models.EmailField()
    telefono = models.IntegerField()
    genero = models.IntegerField()
    documento = models.CharField(max_length=50)
    numerodocumento = models.CharField(max_length=50, null=True)

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
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

# Modelo Planilla.
class Planilla(models.Model):
    fechaInicialPago = models.DateTimeField()
    fechaFinalPago = models.DateTimeField()

# Modelo DetallePlanilla.
class DetallePlanilla(models.Model):
    sueldobruto = models.IntegerField()
    deduccion = models.IntegerField()
    bonificaciones = models.IntegerField()
    detalles = models.CharField(max_length=50)

# ------------------- MODELOS DE EMPLEADO ------------------- #

#Modelo TipoDocumento.
class DocumentoEmpleado(models.Model):
    nombreDocumento = models.CharField(max_length=50)

    def __str__(self):
        return self.nombreDocumento

# Modelo Empleados Cargos
class EmpleadoCargo(models.Model):
    fechaInicio = models.DateTimeField()
    fechaFinal = models.DateTimeField()

#Modelo Cargo
class Cargo(models.Model):
    nombreCargo = models.CharField(max_length=50)
    salario = models.DecimalField(decimal_places=3,max_digits=10)

    def __str__(self):
        return self.nombreCargo

# Modelo Asignacion Clase
class AsignacionClase(models.Model):
    horario = models.DateTimeField()
    fecha = models.DateField()

# Modelo Clase Grupal
class ClaseGrupal(models.Model):
    nombreClase = models.CharField(max_length=50)
    cantidadAlumnos = models.IntegerField()
    class Meta :
        verbose_name_plural = "Clases Grupales"

    def __str__(self):
        return self.nombreClase

# Modelo Salon 
class Salon(models.Model):
    nombreSalon = models.CharField(max_length=50)
    cantidadAlumnos = models.IntegerField()

    class Meta:
        verbose_name_plural = "Salones"

    def __str__(self):
        return self.nombreSalon

#Modelo LogEmpleado
class LogEmpleado(models.Model):
    accion = models.CharField(max_length=50)
    informacion = models.CharField(max_length=100)
    fecha = models.DateTimeField()
    hora = models.TimeField()

""" Modelo de tablas agregadas por el equipo de desarrollo """

class Dieta(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class AsignacionDieta(models.Model):
    fecha = models.DateField()
    hora = models.TimeField()

class Comida(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Rutina(models.Model):
    nombre = models.CharField(max_length=50)
    tipoRutina = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class AsignacionRutina(models.Model):
    series = models.CharField(max_length=50)
    repeticiones = models.CharField(max_length=50)
    descanso = models.CharField(max_length=50)
    capacidad = models.CharField(max_length=50)

class Ejercicio(models.Model):
    nombre = models.CharField(max_length=50)
    imagen = models.ImageField(upload_to='Ejercicios')
    maquina = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Musculo(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre