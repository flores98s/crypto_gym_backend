from django.db import models

# Create your models here.
class TipoMembresia(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.IntegerField()
    descripcion = models.CharField(max_length=100)
