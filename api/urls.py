from rest_framework import routers
from .api import *


router = routers.DefaultRouter()

# url Membresia
router.register('membresia', MembresiaViewSet, 'membresias')
# url tiposmembresia
router.register('tiposmembresia',TipoMembresiaViewSet,'tiposmembresias')
# url precioshistoricomembresia
router.register('precioshistoricomembresia',PrecioHistoricoMembresiaViewSet,'precioshistoricomembresias')
# url descuentos
router.register('descuentos',DescuentoViewSet,'descuentos')
# url cupones
router.register('cupones',CuponesViewSet,'cupones')
# url cliente
router.register('cliente',ClienteViewSet,'clientes')
# url logcliente
router.register('logcliente',LogClienteViewSet,'logclientes')
# url tipodocumentocliente
router.register('tipodocumentocliente',TipoDocumentoClienteViewSet,'tipodocumentoclientes')
# url tipogenerocliente
router.register('tipogenerocliente',TipoGeneroClienteViewSet,'tipogeneroclientes')
# url tiposangrecliente
router.register('tiposangrecliente',TipoSangreClienteViewSet,'tiposangreclientes')
# url medidas
router.register('medidas',MedidasViewSet,'medidas')
# url empleado
router.register('empleado',EmpleadoViewSet,'empleados')
# url tipogenero
router.register('tipogenero',TipoGeneroViewSet,'tipogeneros')
# url planilla
router.register('planilla',PlanillaViewSet,'planillas')
# url detalleplanilla
router.register('detalleplanilla',DetallePlanillaViewSet,'detalleplanillas')
# ------------------- URLS DE EMPLEADO ------------------- #
# url documentoempleado
router.register('documentoempleado',DocumentEmpleadoViewSet,'documentoempleados')
# url empleadocargo
router.register('empleadocargo',EmpleadoCargoViewSet,'empleadoscargos')
# url cargo
router.register('cargo',CargoViewSet,'cargos')
# url asignacionclase
router.register('asignacionclase',AsignacionClaseViewSet,'asignacionclases')
# url clasegrupal
router.register('clasegrupal',ClaseGrupalViewSet,'clasesgrupales')
# url salon
router.register('salon',SalonViewSet,'salones')
# url logcliente
router.register('logempleado',LogEmpleadoViewSet,'logempleados')

urlpatterns = router.urls