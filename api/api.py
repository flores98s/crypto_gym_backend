from .models import *
from rest_framework import viewsets,permissions
from .serializers import *

# api MembresiaViewSet
class MembresiaViewSet(viewsets.ModelViewSet):
    queryset = Membresia.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = MembresiaSerializer

# api TipoMembresiaViewSet
class TipoMembresiaViewSet(viewsets.ModelViewSet):
    queryset = TipoMembresia.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = TipoMembresiaSerializer

# api PrecioHistoricoMembresiaViewSet
class PrecioHistoricoMembresiaViewSet(viewsets.ModelViewSet):
    queryset = PrecioHistoricoMembresia.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = PrecioHistoricoMembresiaSerializer

# api DescuentoViewSet
class DescuentoViewSet(viewsets.ModelViewSet):
    queryset = Descuento.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = DescuentoSerializer

# api CuponesViewSet
class CuponesViewSet(viewsets.ModelViewSet):
    queryset = Cupon.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = CuponSerializer

# api ClienteViewSet
class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ClienteSerializer

# api LogClienteViewSet
class LogClienteViewSet(viewsets.ModelViewSet):
    queryset = LogCliente.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = LogClienteSerializer

# api TipoDocumentoClienteViewSet
class TipoDocumentoClienteViewSet(viewsets.ModelViewSet):
    queryset = TipoDocumentoCliente.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = TipoDocumentoClienteserializer

# api TipoGeneroClienteViewSet
class TipoGeneroClienteViewSet(viewsets.ModelViewSet):
    queryset = TipoGeneroCliente.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = TipoGeneroClienteSerializer

# api TipoSangreClienteViewSet
class TipoSangreClienteViewSet(viewsets.ModelViewSet):
    queryset = TipoGeneroCliente.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = TipoSangreClienteSerializer

# api MedidasViewSet
class MedidasViewSet(viewsets.ModelViewSet):
    queryset = Medidas.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = MedidasSerializer

# api  EmpleadoViewSet
class EmpleadoViewSet(viewsets.ModelViewSet):
    queryset = Empleado.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = EmpleadoSerializer

# api TipoGeneroViewSet
class TipoGeneroViewSet(viewsets.ModelViewSet):
    queryset = TipoGenero.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = TipoGeneroSerializer

# api PlanillaViewSet
class PlanillaViewSet(viewsets.ModelViewSet):
    queryset = Planilla.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = PlanillaSerializer

# api DetallePlanillaViewSet
class DetallePlanillaViewSet(viewsets.ModelViewSet):
    queryset = DetallePlanilla.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = DetallePlanillaSerializer

# ------------------- VIEWSET DE EMPLEADO ------------------- #
# viewset documentoEmpleadoViewSet
class DocumentEmpleadoViewSet(viewsets.ModelViewSet):
    queryset = DocumentoEmpleado.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = DocumentoEmpleadoSerializer

# viewset EmpleadoCargoViewSetViewSet
class EmpleadoCargoViewSet(viewsets.ModelViewSet):
    queryset = EmpleadoCargo.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = EmpleadoCargoSerializer

# viewset CargoViewSet
class CargoViewSet(viewsets.ModelViewSet):
    queryset = Cargo.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = CargoSerializer

# viewset AsignacionClaseViewSet
class AsignacionClaseViewSet(viewsets.ModelViewSet):
    queryset = AsignacionClase.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = AsignacionClaseSerializer

# viewset ClaseGrupalViewSet
class ClaseGrupalViewSet(viewsets.ModelViewSet):
    queryset = ClaseGrupal.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ClaseGrupalSerializer

# viewset SalonViewSet
class SalonViewSet(viewsets.ModelViewSet):
    queryset = Salon.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = SalonSerializer

# viewset LogEmpleadoViewSet
class LogEmpleadoViewSet(viewsets.ModelViewSet):
    queryset = LogEmpleado.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = LogEmpleadoSerializer