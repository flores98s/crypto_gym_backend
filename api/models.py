from django.db import models

# Create your models here.
class TipoMembresia(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.IntegerField()
    descripcion = models.CharField(max_length=100)

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