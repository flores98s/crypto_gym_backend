from rest_framework import serializers
from .models import *


class TipoMembresiaSerializer(serializers.Serializer):
    class Meta:
        model = TipoMembresia
        fields = ['nombre','precio','detalle']

class ClienteSerializer(serializers.Serializer):
    class Meta:
        model = Cliente
        fields = "__all__"