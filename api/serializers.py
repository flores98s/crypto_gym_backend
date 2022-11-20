from rest_framework import serializers
from .models import *
from django.contrib.auth.hashers import make_password

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
class CuponSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cupon
        fields = "__all__"

#Serializar ClienteSerializer
class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = "__all__"

    def create(self, validated_data):
        cliente = Cliente(**validated_data)
        cliente.clave = make_password(cliente.clave)
        cliente.save()
        return cliente

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

    def validate_nombreSangre(self, value):
#         Check if exists
        if TipoSangreCliente.objects.filter(nombreSangre__iexact=value).exists():
            raise serializers.ValidationError("Tipo de sangre ya existe")
        return value

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

    def create(self, validated_data):
        empleado = Empleado(**validated_data)
        empleado.clave = make_password(empleado.clave)
        empleado.save()
        return empleado

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

# ------------------- SERIALIZERS DE EMPLEADO ------------------- #

# serializar TipoDocumentoEmpleadoSerializer
class DocumentoEmpleadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = DocumentoEmpleado
        fields = "__all__"

# serializar EmpleadoCargo
class EmpleadoCargoSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmpleadoCargo
        fields = "__all__"

# serializar TipoCargo
class CargoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cargo
        fields = "__all__"

# serializar TipoClase
class AsignacionClaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = AsignacionClase
        fields = "__all__"

# serializar ClaseGrupal
class ClaseGrupalSerializer(serializers.ModelSerializer):
        class Meta:
            model = ClaseGrupal
            fields = "__all__"
    
# serializar Salon
class SalonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Salon
        fields = "__all__"

# serializar LogEmpleado
class LogEmpleadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = LogEmpleado
        fields = "__all__"   

class dietaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dieta
        fields = ('__all__')

class AsignacionDietaSerializer(serializers.ModelSerializer):
    class Meta:
        model = AsignacionDieta
        fields = ('__all__')

class ComidaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comida
        fields = ('__all__')

    def validate_nombre(self,value):
        if Comida.objects.filter(nombre__iexact=value).exists():
            raise serializers.ValidationError("Comida ya existe")
        return value

    # def validate_nombre(self,value):
    #     if len(value) < 3 :
    #         raise serializers.ValidationError("El nombre debe tener al menos 3 caracteres")

class RutinaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rutina
        fields = ('__all__')

class AsignacionRutinaSerializer(serializers.ModelSerializer):
    class Meta:
        model = AsignacionRutina
        fields = ('__all__')

class EjericioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ejercicio
        fields = ('__all__')

class MusculoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Musculo
        fields = ('__all__')

#-------------------------------------------------------------------------------------------------------------------------------
class FacturaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Factura
        fields = ('__all__')

class ParametrosFacturaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParametrosFactura
        fields = ('__all__')

class ImpuestoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Impuesto
        fields = ('__all__')

class DetalleFacturaSerializer(serializers.ModelSerializer):
    class Meta:
        model = DetalleFactura
        fields = ('__all__')

class DevolucionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Devolucion
        fields = ('__all__')

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = ('__all__')

class DetallesOrdenSerializer(serializers.ModelSerializer):
    class Meta:
        model = DetallesOrden
        fields = ('__all__')

class OrdenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orden
        fields = ('__all__')

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ('__all__')

class PrecioHistoricoProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PrecioHistoricoProducto
        fields = ('__all__')

class CompraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Compra
        fields = ('__all__')

class AdministradorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Administrador
        fields = ('__all__')

class LoginAdministradorSerializer(serializers.ModelSerializer):
    class Meta:
        model = LoginAdministrador
        fields = ('__all__')

class LoginClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ['correo','clave',]
