from rest_framework import serializers
from .models import *


#Serializar TipoMembresiaSerializer
class TipoMembresiaSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoMembresia
        fields = "__all__"

#Serializaer ClienteSerializer
class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = "__all__"

#Serializaer TipoDocumentoClienteserializer
class TipoDocumentoClienteserializer(serializers.ModelSerializer):
    class Meta:
        model = TipoDocumentoCliente
        fields = "__all__"

#Serializaer TipoGeneroClienteSerializer
class TipoGeneroClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoGeneroCliente
        fields = "__all__"

#Serializaer TipoSangreClienteSerializer
class TipoSangreClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoSangreCliente
        fields = "__all__"

#Serializaer MedidasSerializer
class MedidasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medidas
        fields = "__all__"




