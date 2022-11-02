from .models import TipoMembresia
from rest_framework import viewsets,permissions
from .serializers import TipoMembresiaSerializer


class TipoMembresiaViewSet(viewsets.ModelViewSet):
    queryset = TipoMembresia.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = TipoMembresiaSerializer