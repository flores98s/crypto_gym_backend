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
class CuponesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cupones
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

