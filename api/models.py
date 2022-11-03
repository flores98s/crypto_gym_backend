from django.db import models
from django.utils import timezone


# Modelo TipoMembresia.
class TipoMembresia(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.IntegerField()
    descripcion = models.CharField(max_length=100)

# Modelo Cliente.
class Cliente(models.Model):
    nombres = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    clave = models.CharField(max_length=50)
    foto = models.CharField(max_length=50)
    fechaNacimiento = models.DateField()
    documento = models.CharField(max_length=50)
    correo = models.EmailField()
    numeroTelefono = models.IntegerField()
    genero = models.IntegerField()
    grupoSanguineo = models.IntegerField()
    creado = models.DateField(default=timezone.now )

# Modelo TipoDocumentoCliente.
class TipoDocumentoCliente(models.Model):
    nombreDocumento = models.CharField(max_length=50)

# Modelo TipoGeneroCliente.
class TipoGeneroCliente(models.Model):
    nombreGenero = models.CharField(max_length=50)

# Modelo TipoSangreCliente.
class TipoSangreCliente(models.Model):
    nombreSangre = models.CharField(max_length=50)

# Modelo Medidas.
class Medidas(models.Model):
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



