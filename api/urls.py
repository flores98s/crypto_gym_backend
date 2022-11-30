from rest_framework import routers
from .api import *
from django.urls import path, include
from .views import *

router = routers.DefaultRouter()

# url Membresia
router.register('membresia', MembresiaViewSet, 'membresias')
# url tiposmembresia
router.register('tiposmembresia', TipoMembresiaViewSet, 'tiposmembresias')
# url precioshistoricomembresia
router.register('precioshistoricomembresia', PrecioHistoricoMembresiaViewSet, 'precioshistoricomembresias')
# url descuentos
router.register('descuentos', DescuentoViewSet, 'descuentos')
# url cupones
router.register('cupones', CuponesViewSet, 'cupones')
# url cliente
router.register('cliente', ClienteViewSet, 'clientes')
# url logcliente
router.register('logcliente', LogClienteViewSet, 'logclientes')
# url tipodocumentocliente
router.register('tipodocumentocliente', TipoDocumentoClienteViewSet, 'tipodocumentoclientes')
# url tipogenerocliente
router.register('tipogenerocliente', TipoGeneroClienteViewSet, 'tipogeneroclientes')
# url tiposangrecliente
router.register('tiposangrecliente', TipoSangreClienteViewSet, 'tiposangreclientes')
# url medidas
router.register('medidas', MedidasViewSet, 'medidas')
# url empleado
router.register('empleado', EmpleadoViewSet, 'empleados')
# url tipogenero
router.register('tipogenero', TipoGeneroViewSet, 'tipogeneros')
# url planilla
router.register('planilla', PlanillaViewSet, 'planillas')
# url detalleplanilla
router.register('detalleplanilla', DetallePlanillaViewSet, 'detalleplanillas')
# ------------------- URLS DE EMPLEADO ------------------- #
# url documentoempleado
router.register('documentoempleado', DocumentEmpleadoViewSet, 'documentoempleados')
# url empleadocargo
router.register('empleadocargo', EmpleadoCargoViewSet, 'empleadoscargos')
# url cargo
router.register('cargo', CargoViewSet, 'cargos')
# url asignacionclase
router.register('asignacionclase', AsignacionClaseViewSet, 'asignacionclases')
# url clasegrupal
router.register('clasegrupal', ClaseGrupalViewSet, 'clasesgrupales')
# url salon
router.register('salon', SalonViewSet, 'salones')
# url logempleado
router.register('logempleado', LogEmpleadoViewSet, 'logempleados')
# url dieta
router.register('dieta', DietaViewSet, 'dietas')
# url Asignacion Dieta
router.register('asignaciondieta', AsignacionDietaViewSet, 'asignaciondietas')
# url comida
router.register('comida', ComidaViewSet, 'comidas')
# url rutina
router.register('rutina', RutinaViewSet, 'rutinas')
# url Asignacion rutina
router.register('asignacionrutina', AsignacionRutinaViewSet, 'asignacionrutinas')
# url ejercicio
router.register('ejercicio', EjercicioViewSet, 'ejercicios')
# url Musculo
router.register('musculo', MusculoViewSet, 'musculos')
# ------------------------------------------------------------------------------------------------------------------
# url Factura
router.register('factura', FacturaViewSet, 'facturas')
# url Parametros Factura
router.register('parametrosfactura', ParametrosFacturaViewSet, 'parametrosfacturas')
# url Impuesto
router.register('impuesto', ImpuestoViewSet, 'impuestos')
# url Detalle Factura
router.register('detallefactura', DetalleFacturaViewSet, 'detallefacturas')
# url Devolucion
router.register('devolucion', DevolucionViewSet, 'devoluciones')
# url Producto
router.register('producto', ProductoViewSet, 'productos')
# url Detalles Orden
router.register('detallesorden', DetallesOrdenViewSet, 'detallesordenes')
# url Orden
router.register('orden', OrdenViewSet, 'ordenes')
# url Categotia
router.register('categoria', CategoriaViewSet, 'categorias')
# url Precio Historico Producto
router.register('preciohistoricoproducto', PrecioHistoricoProductoViewSet, 'preciohistoricoproductos')
# url Compra
router.register('compra', CompraViewSet, 'compras')
# url Administrador
router.register('administrador', AdministradorViewSet, 'administradores')
# url Login Administrador
router.register('loginadministrador', LoginAdministradorViewSet, 'loginadministradores')
# url Login Cliente
router.register('login', LoginClienteViewSet, 'loginclientes')

urlpatterns = router.urls

urlpatterns += [
    path('empleado/<int:id>', empleado, name='empleado'),
    path('cliente/<int:id>', cliente, name='get_cliente'),
    path('membresia/<int:id>', membresia, name='get_membresia'),
    path('rutina/<int:id>', rutina, name='get_rutina'),
    path('medida/<int:id>', medidas, name='get_medida'),
    path('tiposmembresias/<int:id>', tiposMembresias, name='get_tiposMembresias'),
    path('cargo/<int:id>', cargo, name='get_cargo'),
    path('asignacionrutina/<int:id>', asignacionRutina, name='get_asignacionrutina'),
    path('loginEmpleado/', loginEmpleado, name='loginEmpleado'),
    path('loginCliente/', loginCliente, name='loginCliente'),
    path('ejercicio/<int:id>', ejercicio, name='get_ejercicio'),
    path('dieta/<int:id>', dieta, name='get_dieta'),
    # path('loginEmpleado/', loginEmpleado, name='loginEmpleado'),#
]
