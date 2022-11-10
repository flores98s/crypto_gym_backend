from rest_framework import serializers
from .models import *

#Serializar MembresiaSerializer
class MembresiaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Membresia
        fields = "__all__"

#Serializar TipoMembresiaSerializer
class TipoMembresiaSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoMembresia
        fields = "__all__"

#Serializar PrecioHistoricoMembresiaSerializer
class PrecioHistoricoMembresiaSerializer(serializers.ModelSerializer):
    class Meta:
        model = PrecioHistoricoMembresia
        fields = "__all__"

#Serializar DescuentoSerializer
class DescuentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Descuento
        fields = "__all__"

#Serializar CuponesSerializer
class CuponSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cupon
        fields = "__all__"

#Serializar ClienteSerializer
class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = "__all__"

#Serializar LogClienteSerializer
class LogClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = LogCliente
        fields = "__all__"

#Serializar TipoDocumentoClienteserializer
class TipoDocumentoClienteserializer(serializers.ModelSerializer):
    class Meta:
        model = TipoDocumentoCliente
        fields = "__all__"

#Serializar TipoGeneroClienteSerializer
class TipoGeneroClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoGeneroCliente
        fields = "__all__"

#Serializar TipoSangreClienteSerializer
class TipoSangreClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoSangreCliente
        fields = "__all__"

#Serializar MedidasSerializer
class MedidasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medidas
        fields = "__all__"

#Serializar EmpleadoSerializer
class EmpleadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empleado
        fields = "__all__"

#Serializar TipoGeneroSerializer
class TipoGeneroSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoGenero
        fields = "__all__"

#Serializar PlanillaSerializer
class PlanillaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Planilla
        fields = "__all__"

#Serializar DetallePlanillaSerializer
class DetallePlanillaSerializer(serializers.ModelSerializer):
    class Meta:
        model = DetallePlanilla
        fields = "__all__"

# ------------------- SERIALIZERS DE EMPLEADO ------------------- #

# serializar TipoDocumentoEmpleadoSerializer
class DocumentoEmpleadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = DocumentoEmpleado
        fields = "__all__"

# serializar EmpleadoCargo
class EmpleadoCargoSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmpleadoCargo
        fields = "__all__"

# serializar TipoCargo
class CargoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cargo
        fields = "__all__"

# serializar TipoClase
class AsignacionClaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = AsignacionClase
        fields = "__all__"

# serializar ClaseGrupal
class ClaseGrupalSerializer(serializers.ModelSerializer):
        class Meta:
            model = ClaseGrupal
            fields = "__all__"
    
# serializar Salon
class SalonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Salon
        fields = "__all__"

# serializar LogEmpleado
class LogEmpleadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = LogEmpleado
        fields = "__all__"   

class dietaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dieta
        fields = ('__all__')

class AsignacionDietaSerializer(serializers.ModelSerializer):
    class Meta:
        model = AsignacionDieta
        fields = ('__all__')

class ComidaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comida
        fields = ('__all__')

class RutinaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rutina
        fields = ('__all__')

class AsignacionRutinaSerializer(serializers.ModelSerializer):
    class Meta:
        model = AsignacionRutina
        fields = ('__all__')

class EjericioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ejercicio
        fields = ('__all__')

class MusculoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Musculo
        fields = ('__all__')