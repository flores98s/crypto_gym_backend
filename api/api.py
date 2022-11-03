from .models import *
from rest_framework import viewsets,permissions
from .serializers import *

# api TipoMembresiaViewSet
class TipoMembresiaViewSet(viewsets.ModelViewSet):
    queryset = TipoMembresia.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = TipoMembresiaSerializer

# api ClienteViewSet
class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ClienteSerializer

# api TipoDocumentoClienteViewSet
class TipoDocumentoClienteViewSet(viewsets.ModelViewSet):
    queryset = TipoDocumentoCliente.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = TipoDocumentoClienteserializer

# api TipoGeneroClienteViewSet
class TipoGeneroClienteViewSet(viewsets.ModelViewSet):
    queryset = TipoGeneroCliente.objects.all()
    permission_classes = [permissions.AllowAny]
    serializers_class = TipoGeneroClienteSerializer

# api TipoSangreClienteViewSet
class TipoSangreClienteViewSet(viewsets.ModelViewSet):
    queryset = TipoGeneroCliente.objects.all()
    permission_classes = [permissions.AllowAny]
    serializers_class = TipoSangreClienteSerializer

# api MedidasViewSet(viewsets
class MedidasViewSet(viewsets.ModelViewSet):
    queryset = Medidas.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = TipoSangreClienteSerializer


