from django.forms import model_to_dict
from django.shortcuts import render
from .models import *
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.hashers import make_password, check_password
from datetime import datetime, date, timedelta
from .utilidades.exportar import generar_csv, generar_pdf

# Create your views here.

@csrf_exempt
def empleado(request, id):
    if request.method == 'GET':

        empleados = list(Empleado.objects.filter(id=id).values())
        if empleados:
            return JsonResponse({'data': empleados}, safe=False)
        else:
            return JsonResponse({'data': 'No se encontró el id'}, safe=False)
        return JsonResponse({'data': empleados}, safe=False)

    elif request.method == 'POST':
        data = json.loads(request.body)
        empleado = Empleado.objects.create(**data)
        return JsonResponse({'data': 'Empleado creado'}, safe=False)

    elif request.method == 'PUT':
        data = json.loads(request.body)
        empleado = Empleado.objects.filter(id=id).update(**data)
        return JsonResponse({'data': 'Empleado actualizado'}, safe=False)

    elif request.method == 'DELETE':
        empleado = Empleado.objects.filter(id=id)
        if empleado:
            empleado.delete()
            return JsonResponse({'data': 'Empleado eliminado'}, safe=False)
        else:
            return JsonResponse({'data': 'No se encontró el id'}, safe=False)
    return JsonResponse({'data': 'Empleado eliminado'}, safe=False)


@csrf_exempt
def cliente(request, id):
    if request.method == 'POST':
        clientes = list(Cliente.objects.filter(id=id).values())
        if clientes:
            return JsonResponse({'data': clientes}, safe=False)
        else:
            return JsonResponse({'data': 'No se encontró el id'}, safe=False)
        return JsonResponse({'data': clientes}, safe=False)
    if request.method == 'GET':
        clientes = list(Cliente.objects.filter(id=id).values())
        if clientes:
            return JsonResponse({'data': clientes}, safe=False)
        else:
            return JsonResponse({'data': 'No se encontró el id'}, safe=False)
        return JsonResponse({'data': clientes}, safe=False)
    elif request.method == 'DELETE':
        cliente = Cliente.objects.get(id=id)
        if cliente:
            cliente.delete()
            return JsonResponse({'data': 'Cliente eliminado'}, safe=False)
        else:
            return JsonResponse({'data': 'No se encontró el id'}, safe=False)

    elif request.method == 'PUT':
        cliente = Cliente.objects.get(id=id)
        if cliente:
            data = json.loads(request.body)
            cliente.nombres = data['nombre']
            cliente.apellidos = data['apellido']
            cliente.save()
            return JsonResponse({'data': 'Cliente actualizado'}, safe=False)
        else:
            return JsonResponse({'data': 'No se encontró el id'}, safe=False)
    return JsonResponse({'data': 'No se encontró el id'}, safe=False)


def rutina(request,id):
    if request.method == 'GET':
        rutinas = list(Rutina.objects.filter(id=id).values())
        return JsonResponse({'data': rutinas}, safe=False)
    elif request.method == 'POST':
        data = json.loads(request.body)
        rutina = Rutina.objects.create(**data)
        return JsonResponse({'data': 'Rutina creada'}, safe=False)
    elif request.method == 'PUT':
        data = json.loads(request.body)
        rutina = Rutina.objects.filter(id=id).update(**data)
        return JsonResponse({'data': 'Rutina actualizada'}, safe=False)
    elif request.method == 'DELETE':
        rutina = Rutina.objects.filter(id=id)
        if rutina:
            rutina.delete()
            return JsonResponse({'data': 'Rutina eliminada'}, safe=False)
        else:
            return JsonResponse({'data': 'No se encontró el id'}, safe=False)
        return JsonResponse({'data': 'Rutina eliminada'}, safe=False)
    return JsonResponse({'data': 'No se encontró el id'}, safe=False)


def membresia(request):
    if request.method == 'GET':
        membresias = list(Membresia.objects.all().values())
        return JsonResponse({'data': membresias}, safe=False)
    elif request.method == 'POST':
        data = json.loads(request.body)
        membresia = Membresia.objects.create(**data)
        return JsonResponse({'data': 'Membresia creada'}, safe=False)
    elif request.method == 'PUT':
        data = json.loads(request.body)
        membresia = Membresia.objects.filter(id=id).update(**data)
        return JsonResponse({'data': 'Membresia actualizada'}, safe=False)
    elif request.method == 'DELETE':
        membresia = Membresia.objects.filter(id=id)
        if membresia:
            membresia.delete()
            return JsonResponse({'data': 'Membresia eliminada'}, safe=False)
        else:
            return JsonResponse({'data': 'No se encontró el id'}, safe=False)
        return JsonResponse({'data': 'Membresia eliminada'}, safe=False)
    return JsonResponse({'data': 'No se encontró el id'}, safe=False)


@csrf_exempt
def medidas(request, id):
    if request.method == 'GET':
        medidas = list(Medidas.objects.filter(id=id).values())
        if medidas:
            return JsonResponse({'data': medidas}, safe=False)
        else:
            return JsonResponse({'data': 'No se encontró el id'}, safe=False)
        return JsonResponse({'data': medidas}, safe=False)
    elif request.method == 'POST':
        data = json.loads(request.body)
        medidas = Medidas.objects.create(**data)
        return JsonResponse({'data': 'Medidas creadas'}, safe=False)
    elif request.method == 'PUT':
        data = json.loads(request.body)
        medidas = Medidas.objects.filter(id=id).update(**data)
        return JsonResponse({'data': 'Medidas actualizadas'}, safe=False)
    elif request.method == 'DELETE':
        medidas = Medidas.objects.filter(id=id)
        if medidas:
            medidas.delete()
            return JsonResponse({'data': 'Medidas eliminadas'}, safe=False)
        else:
            return JsonResponse({'data': 'No se encontró el id'}, safe=False)
        return JsonResponse({'data': 'Medidas eliminadas'}, safe=False)
    return JsonResponse({'data': 'No se encontró el id'}, safe=False)


@csrf_exempt
def tiposMembresias(request, id):
    if request.method == 'GET':
        tiposMembresias = list(TipoMembresia.objects.filter(id=id).values())
        if tiposMembresias:
            return JsonResponse({'data': tiposMembresias}, safe=False)
        else:
            return JsonResponse({'data': 'No se encontró el id'}, safe=False)
    elif request.method == 'POST':
        data = json.loads(request.body)
        tiposMembresias = TipoMembresia.objects.create(**data)
        return JsonResponse({'data': 'Tipo de membresia creada'}, safe=False)
    elif request.method == 'PUT':
        data = json.loads(request.body)
        tiposMembresias = TipoMembresia.objects.filter(id=id).update(**data)
        return JsonResponse({'data': 'Tipo de membresia actualizada'}, safe=False)
    elif request.method == 'DELETE':
        tiposMembresias = TipoMembresia.objects.filter(id=id)
        if tiposMembresias:
            tiposMembresias.delete()
            return JsonResponse({'data': 'Tipo de membresia eliminada'}, safe=False)
        else:
            return JsonResponse({'data': 'No se encontró el id'}, safe=False)
        return JsonResponse({'data': 'Tipo de membresia eliminada'}, safe=False)
    return JsonResponse({'data': 'No se encontró el id'}, safe=False)


@csrf_exempt
def cargo(request, id):
    if request.method == 'GET':
        cargos = list(Cargo.objects.filter(id=id).values())
        if cargos:
            return JsonResponse({'data': cargos}, safe=False)
        else:
            return JsonResponse({'data': 'No se encontró el id'}, safe=False)
    elif request.method == 'POST':
        data = json.loads(request.body)
        cargos = Cargo.objects.create(**data)
        return JsonResponse({'data': 'Cargo creado'}, safe=False)
    elif request.method == 'PUT':
        data = json.loads(request.body)
        cargos = Cargo.objects.filter(id=id).update(**data)
        return JsonResponse({'data': 'Cargo actualizado'}, safe=False)
    elif request.method == 'DELETE':
        cargos = Cargo.objects.filter(id=id)
        if cargos:
            cargos.delete()
            return JsonResponse({'data': 'Cargo eliminado'}, safe=False)
        else:
            return JsonResponse({'data': 'No se encontró el id'}, safe=False)
    return JsonResponse({'data': 'Cargo eliminado'}, safe=False)


@csrf_exempt
def asignacionRutina(request, id):
    if request.method == 'GET':
        asignacionRutinas = list(AsignacionRutina.objects.filter(id=id).values())
        if asignacionRutinas:
            return JsonResponse({'data': asignacionRutinas}, safe=False)
        else:
            return JsonResponse({'data': 'No se encontró el id'}, safe=False)
    elif request.method == 'POST':
        data = json.loads(request.body)
        asignacionRutinas = AsignacionRutina.objects.create(**data)
        return JsonResponse({'data': 'Asignacion de rutina creada'}, safe=False)
    elif request.method == 'PUT':
        data = json.loads(request.body)
        asignacionRutinas = AsignacionRutina.objects.filter(id=id).update(**data)
        return JsonResponse({'data': 'Asignacion de rutina actualizada'}, safe=False)
    elif request.method == 'DELETE':
        asignacionRutinas = AsignacionRutina.objects.filter(id=id)
        if asignacionRutinas:
            asignacionRutinas.delete()
            return JsonResponse({'data': 'Asignacion de rutina eliminada'}, safe=False)
        else:
            return JsonResponse({'data': 'No se encontró el id'}, safe=False)
    return JsonResponse({'data': 'Asignacion de rutina eliminada'}, safe=False)


@csrf_exempt
def loginCliente(request):
    data = json.loads(request.body)
    correo = data['correo']
    clave = data['clave']

    if request.method == 'POST':
        cliente = Cliente.objects.filter(correo=correo).first()
        print(cliente)
        # check if cliente is blocked
        if cliente:
            if cliente.bloqueado == 'bloqueado':
                return JsonResponse({'auth': False, 'error': 'Usuario bloqueado'}, safe=False)
            else:
                if check_password(clave, cliente.clave):
                    data = model_to_dict(cliente)
                    data['foto'] = str(data['foto'])
                    return JsonResponse([{'auth': True, 'data': data}], safe=False)
                else:
                    if cliente.intentos < 3:
                        cliente.intentos = cliente.intentos + 1
                        cliente.save()
                        return JsonResponse({'auth': False, 'error': 'Usuario o Contraseña incorrecta'}, safe=False)
                    elif cliente.intentos == 3:
                        cliente.bloqueado = True
                        cliente.save()
        return JsonResponse({'auth': False, 'error': 'Usuario bloqueado'}, safe=False)
    else:
        return JsonResponse({'auth': False, 'data': 'Usuario no encontrado'}, safe=False)


@csrf_exempt
def ejercicio(request, id):
    if request.method == 'GET':
        ejercicios = list(Ejercicio.objects.filter(id=id).values())
        if ejercicios:
            return JsonResponse({'data': ejercicios}, safe=False)
        else:
            return JsonResponse({'data': 'No se encontró el id'}, safe=False)
    elif request.method == 'POST':
        data = json.loads(request.body)
        ejercicios = Ejercicio.objects.create(**data)
        return JsonResponse({'data': 'Ejercicio creado'}, safe=False)
    elif request.method == 'PUT':
        data = json.loads(request.body)
        ejercicios = Ejercicio.objects.filter(id=id).update(**data)
        return JsonResponse({'data': 'Ejercicio actualizado'}, safe=False)
    elif request.method == 'DELETE':
        ejercicios = Ejercicio.objects.filter(id=id)
        if ejercicios:
            ejercicios.delete()
            return JsonResponse({'data': 'Ejercicio eliminado'}, safe=False)
        else:
            return JsonResponse({'data': 'No se encontró el id'}, safe=False)
    return JsonResponse({'data': 'Ejercicio eliminado'}, safe=False)


@csrf_exempt
def loginEmpleado(request):
    data = json.loads(request.body)
    correo = data['correo']
    clave = data['clave']

    if request.method == 'POST':
        empleado = Empleado.objects.filter(correo=correo).first()
        print(empleado)
        # check if empleado is blocked
        if empleado:
            if empleado.bloqueado == 'bloqueado':
                return JsonResponse({'auth': False, 'error': 'Usuario bloqueado'}, safe=False)
            else:
                if check_password(clave, empleado.clave):
                    data = model_to_dict(empleado)
                    return JsonResponse([{'auth': True, 'data': data}], safe=False)
                else:
                    if empleado.intentos < 3:
                        empleado.intentos = empleado.intentos + 1
                        empleado.save()
                        return JsonResponse({'auth': False, 'error': 'Usuario o Contraseña incorrecta'}, safe=False)
                    elif empleado.intentos == 3:
                        empleado.bloqueado = True
                        empleado.save()
        return JsonResponse({'auth': False, 'error': 'Usuario bloqueado'}, safe=False)
    else:
        return JsonResponse({'auth': False, 'data': 'Usuario no encontrado'}, safe=False)


@csrf_exempt
def dieta(request, id):
    if request.method == 'GET':
        dietas = list(Dieta.objects.filter(id=id).values())
        if dietas:
            return JsonResponse({'data': dietas}, safe=False)
        else:
            return JsonResponse({'data': 'No se encontró el id'}, safe=False)
    elif request.method == 'POST':
        data = json.loads(request.body)
        dietas = Dieta.objects.create(**data)
        return JsonResponse({'data': 'Dieta creada'}, safe=False)
    elif request.method == 'PUT':
        data = json.loads(request.body)
        dietas = Dieta.objects.filter(id=id).update(**data)
        return JsonResponse({'data': 'Dieta actualizada'}, safe=False)
    elif request.method == 'DELETE':
        dietas = Dieta.objects.filter(id=id)
        if dietas:
            dietas.delete()
        return JsonResponse({'data': 'Dieta eliminada'}, safe=False)
    else:
        return JsonResponse({'data': 'No se encontró el id'}, safe=False)


@csrf_exempt
def parametrosFactura(request):

    if request.method == 'GET':
        # parametrosFacturas = ParametrosFactura.objects.latest('id')
        parametrosFacturas = ParametrosFactura.objects.filter(activo=True).first()


        if parametrosFacturas:
            if str(parametrosFacturas.ultimaFactura) == str(parametrosFacturas.rangoFinal):
                parametrosFacturas.activo = False
                parametrosFacturas.save()

                cai = parametrosFacturas.cai
                cai = cai.split('-')
                cai[-1] = str(int(cai[-1]) + 1)
                cai = '-'.join(cai)


            #     crear nueva parametrosFactura con rango inicial y final
                parametrosFacturas = ParametrosFactura.objects.create(
                    rangoInicial=parametrosFacturas.rangoFinal+1,
                    rangoFinal=parametrosFacturas.rangoFinal+500,
                    ultimaFactura=parametrosFacturas.rangoFinal+1,
                    cai=cai,
                    fechaEmision= date.today(),
                    fechaVencimiento= date.today() + timedelta(days=30),
                    codigoSucursal=parametrosFacturas.codigoSucursal,
                )
                parametrosFacturas.save()
                return JsonResponse({'data': model_to_dict(parametrosFacturas)}, safe=False)

            return JsonResponse({'data': model_to_dict(parametrosFacturas)}, safe=False)
        else:
            return JsonResponse({'data': 'No se encontró el id'}, safe=False)
    elif request.method == 'POST':
        data = json.loads(request.body)
        parametrosFacturas = ParametrosFactura.objects.create(**data)
        return JsonResponse({'data': 'Parametros de factura creados'}, safe=False)
    elif request.method == 'PUT':
        data = json.loads(request.body)
        parametrosFacturas = ParametrosFactura.objects.filter(id=id).update(**data)
        return JsonResponse({'data': 'Parametros de factura actualizados'}, safe=False)
    elif request.method == 'DELETE':
        parametrosFacturas = ParametrosFactura.objects.filter(id=id)
        if parametrosFacturas:
            parametrosFacturas.delete()
            return JsonResponse({'data': 'Parametros de factura eliminados'}, safe=False)
        else:
            return JsonResponse({'data': 'No se encontró el id'}, safe=False)
    return JsonResponse({'data': 'Parametros de factura eliminados'}, safe=False)


@csrf_exempt
def empleadoCargo(request, id):
    if request.method == 'GET':
        empleadosCargos = list(EmpleadoCargo.objects.filter(id=id).values())
        if empleadosCargos:
            return JsonResponse({'data': empleadosCargos}, safe=False)
        else:
            return JsonResponse({'data': 'No se encontró el id'}, safe=False)
    elif request.method == 'POST':
        data = json.loads(request.body)
        empleadosCargos = EmpleadoCargo.objects.create(**data)
        return JsonResponse({'data': 'EmpleadoCargo creado'}, safe=False)
    elif request.method == 'PUT':
        data = json.loads(request.body)
        empleadosCargos = EmpleadoCargo.objects.filter(id=id).update(**data)
        return JsonResponse({'data': 'EmpleadoCargo actualizado'}, safe=False)
    elif request.method == 'DELETE':
        empleadosCargos = EmpleadoCargo.objects.filter(id=id)
        if empleadosCargos:
            empleadosCargos.delete()
            return JsonResponse({'data': 'EmpleadoCargo eliminado'}, safe=False)
        else:
            return JsonResponse({'data': 'No se encontró el id'}, safe=False)
    return JsonResponse({'data': 'EmpleadoCargo eliminado'}, safe=False)


@csrf_exempt
def detallePlanilla(request, id):
    if request.method == 'GET':
        detallesPlanillas = list(DetallePlanilla.objects.filter(id=id).values())
        if detallesPlanillas:
            return JsonResponse({'data': detallesPlanillas}, safe=False)
        else:
            return JsonResponse({'data': 'No se encontró el id'}, safe=False)
    elif request.method == 'POST':
        data = json.loads(request.body)
        detallesPlanillas = DetallePlanilla.objects.create(**data)
        return JsonResponse({'data': 'DetallePlanilla creado'}, safe=False)
    elif request.method == 'PUT':
        data = json.loads(request.body)
        detallesPlanillas = DetallePlanilla.objects.filter(id=id).update(**data)
        return JsonResponse({'data': 'DetallePlanilla actualizado'}, safe=False)
    elif request.method == 'DELETE':
        detallesPlanillas = DetallePlanilla.objects.filter(id=id)
        if detallesPlanillas:
            detallesPlanillas.delete()
            return JsonResponse({'data': 'DetallePlanilla eliminado'}, safe=False)
        else:
            return JsonResponse({'data': 'No se encontró el id'}, safe=False)
    return JsonResponse({'data': 'DetallePlanilla eliminado'}, safe=False)


@csrf_exempt
def planilla(request, id):
    if request.method == 'GET':
        planillas = list(Planilla.objects.filter(id=id).values())
        if planillas:
            return JsonResponse({'data': planillas}, safe=False)
        else:
            return JsonResponse({'data': 'No se encontró el id'}, safe=False)
    elif request.method == 'POST':
        data = json.loads(request.body)
        planillas = Planilla.objects.create(**data)
        return JsonResponse({'data': 'Planilla creada'}, safe=False)
    elif request.method == 'PUT':
        data = json.loads(request.body)
        planillas = Planilla.objects.filter(id=id).update(**data)
        return JsonResponse({'data': 'Planilla actualizada'}, safe=False)
    elif request.method == 'DELETE':
        planillas = Planilla.objects.filter(id=id)
        if planillas:
            planillas.delete()
            return JsonResponse({'data': 'Planilla eliminada'}, safe=False)
        else:
            return JsonResponse({'data': 'No se encontró el id'}, safe=False)
    return JsonResponse({'data': 'Planilla eliminada'}, safe=False)


@csrf_exempt
def membresiasClientes(request, id):
    if request.method == 'GET':
        membresiasCliente = Membresia.objects.filter(cliente=id).values()

        if len(membresiasCliente) <= 0:
            return JsonResponse({'data': 'No tienes suscripcion activa', "suscripcionActiva": False,}, safe=False)
        tipoMembresia = TipoMembresia.objects.filter(id=membresiasCliente[0]['tipoMembresia_id']).values()

        if membresiasCliente:
            membresiasCliente = membresiasCliente[0]
            membresiasCliente['NombreMembresia'] = tipoMembresia[0]['nombreMembresia']
            membresiasCliente['descripcionMembresia'] = tipoMembresia[0]['descripcion']
            membresiasCliente['precioMembresia'] = tipoMembresia[0]['precio']
            membresiasCliente['tiempoRestanteDias'] = (membresiasCliente['fechaFinal'] - datetime.now(timezone.utc)).days
            membresiasCliente['SuscripcionActiva'] = True
            return JsonResponse(membresiasCliente, safe=False)
        else:
            return JsonResponse({'error': "No se encontro Cliente"})


@csrf_exempt
def actualizarUltimaFactura(request, id):
    if request.method == 'GET':
        parametrosFactura = ParametrosFactura.objects.latest('id')
        if parametrosFactura:
            parametrosFactura.ultimaFactura = parametrosFactura.ultimaFactura + 1
            parametrosFactura.save()
            return JsonResponse({'data': "Ultima factura actualizada"}, safe=False)

        else:
            return JsonResponse({'data': 'No se encontró el id'}, safe=False)


@csrf_exempt
def getFacturaById(request, id):
    if request.method == 'GET':
        factura = Factura.objects.filter(id=id).values()
        factura = factura[0]
        factura['detalleFactura'] = DetalleFactura.objects.filter(id=factura['detalleFactura_id']).values()[0]
        factura['producto'] = Producto.objects.filter(id=factura['detalleFactura']['producto_id']).values()[0]
        factura['cliente'] = Cliente.objects.filter(id=factura['cliente_id']).values()[0]
        # factura['membresia'] = Membresia.objects.filter(id=factura['membresia_id']).values()[0]
        # factura['tipoMembresia'] = TipoMembresia.objects.filter(id = factura['membresia']['tipoMembresia_id']).values()[0]
        factura['parametrosFactura'] = ParametrosFactura.objects.filter(id=factura['parametrosFactura_id']).values()[0]



        if factura:
            return JsonResponse({'data': factura}, safe=False)
        else:
            return JsonResponse({'data': 'No se encontró el id'}, safe=False)
    return JsonResponse({'data': 'No se encontró el id'}, safe=False)


@csrf_exempt
def getFacturaByCliente(request, id):
    if request.method == 'GET':
        factura = list(Factura.objects.filter(cliente=id).order_by('-id').values())
        if factura:
            return JsonResponse({'data': factura}, safe=False)
        else:
            return JsonResponse({'data': 'No se encontró el id'}, safe=False)
        if factura:
            return JsonResponse({'data': factura}, safe=False)
        else:
            return JsonResponse({'data': 'No se encontró el id'}, safe=False)
    return JsonResponse({'data': 'No se encontró el id'}, safe=False)

@csrf_exempt
def getRutinasByCliente(request, id):
    if request.method == 'GET':
        rutinas = list(Rutina.objects.filter(cliente=id).values())
        if rutinas:
            return JsonResponse({'data': rutinas}, safe=False)
        else:
            return JsonResponse({'data': 'No se encontró el id'}, safe=False)
    return JsonResponse({'data': 'No se encontró el id'}, safe=False)

@csrf_exempt
def getDietasByCliente(request, id):
    if request.method == 'GET':
        dietas = list(Dieta.objects.filter(cliente=id).values())
        if dietas:
            return JsonResponse({'data': dietas}, safe=False)
        else:
            return JsonResponse({'data': 'No se encontró el id'}, safe=False)
    return JsonResponse({'data': 'No se encontró el id'}, safe=False)

@csrf_exempt
def getAsignacionClaseByCliente(request, id):
    if request.method == 'GET':
        asignacionClase = list(AsignacionClase.objects.filter(cliente=id).values())
        if asignacionClase:
            return JsonResponse({'data': asignacionClase}, safe=False)
        else:
            return JsonResponse({'data': 'No se encontró el id'}, safe=False)
    return JsonResponse({'data': 'No se encontró el id'}, safe=False)

@csrf_exempt
def getMedidasByCliente(request, id):
    if request.method == 'GET':
        medidas = list(Medidas.objects.filter(cliente=id).values())
        if medidas:
            return JsonResponse({'data': medidas}, safe=False)
        else:
            return JsonResponse({'data': 'No se encontró el id'}, safe=False)
    return JsonResponse({'data': 'No se encontró el id'}, safe=False)

@csrf_exempt
def exportEmpleadosCSV(request):
    if request.method == "GET":
        response = generar_csv(request, 'Empleado')
        return response
    
@csrf_exempt
def exportEmpleadosPDF(request):
    if request.method == "GET":
        response = generar_pdf(request, 'Empleado')
        return response