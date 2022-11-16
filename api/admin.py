from django.contrib import admin
from .models import *


# Register your models here.


admin.site.register(Membresia)
admin.site.register(TipoMembresia)
admin.site.register(PrecioHistoricoMembresia)
admin.site.register(Descuento)
admin.site.register(Cupon)
admin.site.register(TipoSangreCliente)
admin.site.register(Cliente)
admin.site.register(LogCliente)
admin.site.register(TipoDocumentoCliente)
admin.site.register(TipoGeneroCliente)
admin.site.register(Medidas)
admin.site.register(Empleado)
admin.site.register(TipoGenero)
admin.site.register(Planilla)
admin.site.register(DetallePlanilla)
admin.site.register(DocumentoEmpleado)
admin.site.register(EmpleadoCargo)
admin.site.register(Cargo)
admin.site.register(AsignacionClase)
admin.site.register(ClaseGrupal)
admin.site.register(Salon)
admin.site.register(LogEmpleado)
admin.site.register(Dieta)
admin.site.register(AsignacionDieta)
admin.site.register(Comida)
admin.site.register(Rutina)
admin.site.register(AsignacionRutina)
admin.site.register(Ejercicio)
admin.site.register(Musculo)
#-------------------------------------------------------------------------------------------------------------------------------
admin.site.register(Factura)
admin.site.register(ParametrosFactura)
admin.site.register(Impuesto)
admin.site.register(DetalleFactura)
admin.site.register(Devolucion)
admin.site.register(Producto)
admin.site.register(DetallesOrden)
admin.site.register(Orden)
admin.site.register(Categoria)
admin.site.register(PrecioHistoricoProducto)
admin.site.register(Compra)
admin.site.register(Administrador)
admin.site.register(LoginAdministrador)




