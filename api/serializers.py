from rest_framework import serializers
from .models import TipoMembresia


class TipoMembresiaSerializer(serializers.Serializer):
    class Meta:
        model = TipoMembresia
        fields = ['nombre','precio','detalle']

