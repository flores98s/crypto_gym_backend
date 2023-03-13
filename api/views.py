from django.forms import model_to_dict
from django.shortcuts import render
from .models import *
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.hashers import make_password, check_password
from datetime import datetime, date, timedelta
from .utilidades.exportar import generar_csv, generar_pdf
import logging
from api.models import LogEntry

logger = logging.getLogger(__name__)
# Create your views here.

@csrf_exempt
def empleado(request, id):
    if request.method == 'GET':

        empleados = list(Empleado.objects.filter(id=id).values())
        if empleados:
            logger.info("Se obtuvo el empleado con id: " + str(id))
            return JsonResponse({'data': empleados}, safe=False)
        else:
            logger.error("No se encontró el empleado con id: " + str(id))
            return JsonResponse({'data': 'No se encontró el id'}, safe=False)
        return JsonResponse({'data': empleados}, safe=False)

    elif request.method == 'POST':

        data = json.loads(request.body)
        empleado = Empleado.objects.create(**data)
        logger.info("Se creo el empleado con id: " + str(id))
        return JsonResponse({'data': 'Empleado creado'}, safe=False)

    elif request.method == 'PUT':
        data = json.loads(request.body)
        empleado = Empleado.objects.filter(id=id).update(**data)
        logger.info("Se actualizo el empleado con id: " + str(id))
        return JsonResponse({'data': 'Empleado actualizado'}, safe=False)

    elif request.method == 'DELETE':
        empleado = Empleado.objects.filter(id=id)
        if empleado:
            empleado.delete()
            logger.info("Se elimino el empleado con id: " + str(id))
            return JsonResponse({'data': 'Empleado eliminado'}, safe=False)
        else:
            logger.error("No se encontró el empleado con id: " + str(id))
            return JsonResponse({'data': 'No se encontró el id'}, safe=False)
    return JsonResponse({'data': 'Empleado eliminado'}, safe=False)


@csrf_exempt
def cliente(request, id):
    if request.method == 'POST':
        clientes = list(Cliente.objects.filter(id=id).values())
        if clientes:
            logger.info("Se obtuvo el cliente con id: " + str(id))
            return JsonResponse({'data': clientes}, safe=False)
        else:
            logger.error("No se encontró el cliente con id: " + str(id))
            return JsonResponse({'data': 'No se encontró el id'}, safe=False)
        return JsonResponse({'data': clientes}, safe=False)
    if request.method == 'GET':
        clientes = list(Cliente.objects.filter(id=id).values())
        if clientes:
            logger.info("Se obtuvo el cliente con id: " + str(id))
            return JsonResponse({'data': clientes}, safe=False)
        else:
            logger.error("No se encontró el cliente con id: " + str(id))
            return JsonResponse({'data': 'No se encontró el id'}, safe=False)
        return JsonResponse({'data': clientes}, safe=False)
    elif request.method == 'DELETE':
        cliente = Cliente.objects.get(id=id)
        if cliente:
            cliente.delete()
            logger.info("Se elimino el cliente con id: " + str(id))
            return JsonResponse({'data': 'Cliente eliminado'}, safe=False)
        else:
            logger.error("No se encontró el cliente con id: " + str(id))
            return JsonResponse({'data': 'No se encontró el id'}, safe=False)

    elif request.method == 'PUT':
        cliente = Cliente.objects.get(id=id)
        if cliente:
            data = json.loads(request.body)
            cliente.nombres = data['nombre']
            cliente.apellidos = data['apellido']
            cliente.save()
            logger.info("Se actualizo el cliente con id: " + str(id))
            return JsonResponse({'data': 'Cliente actualizado'}, safe=False)
        else:
            logger.error("No se encontró el cliente con id: " + str(id))
            return JsonResponse({'data': 'No se encontró el id'}, safe=False)
    return JsonResponse({'data': 'No se encontró el id'}, safe=False)


def rutina(request,id):
    if request.method == 'GET':
        rutinas = list(Rutina.objects.filter(id=id).values())
        logger.info("Se obtuvo la rutina con id: " + str(id))
        return JsonResponse({'data': rutinas}, safe=False)
    elif request.method == 'POST':
        data = json.loads(request.body)
        rutina = Rutina.objects.create(**data)
        logger.info("Se creo la rutina con id: " + str(id))
        return JsonResponse({'data': 'Rutina creada'}, safe=False)
    elif request.method == 'PUT':
        data = json.loads(request.body)
        rutina = Rutina.objects.filter(id=id).update(**data)
        logger.info("Se actualizo la rutina con id: " + str(id))
        return JsonResponse({'data': 'Rutina actualizada'}, safe=False)
    elif request.method == 'DELETE':
        rutina = Rutina.objects.filter(id=id)
        if rutina:
            rutina.delete()
            logger.info("Se elimino la rutina con id: " + str(id))
            return JsonResponse({'data': 'Rutina eliminada'}, safe=False)
        else:
            logger.error("No se encontró la rutina con id: " + str(id))
            return JsonResponse({'data': 'No se encontró el id'}, safe=False)

        return JsonResponse({'data': 'Rutina eliminada'}, safe=False)
    return JsonResponse({'data': 'No se encontró el id'}, safe=False)


def membresia(request):
    if request.method == 'GET':
        membresias = list(Membresia.objects.all().values())
        logger.info("Se obtuvo la membresia con id: " + str(id))
        return JsonResponse({'data': membresias}, safe=False)
    elif request.method == 'POST':
        data = json.loads(request.body)
        membresia = Membresia.objects.create(**data)
        logger.info("Se creo la membresia con id: " + str(id))
        return JsonResponse({'data': 'Membresia creada'}, safe=False)
    elif request.method == 'PUT':
        data = json.loads(request.body)
        membresia = Membresia.objects.filter(id=id).update(**data)
        logger.info("Se actualizo la membresia con id: " + str(id))
        return JsonResponse({'data': 'Membresia actualizada'}, safe=False)
    elif request.method == 'DELETE':
        membresia = Membresia.objects.filter(id=id)
        if membresia:
            membresia.delete()
            logger.info("Se elimino la membresia con id: " + str(id))
            return JsonResponse({'data': 'Membresia eliminada'}, safe=False)
        else:
            logger.error("No se encontró la membresia con id: " + str(id))
            return JsonResponse({'data': 'No se encontró el id'}, safe=False)
        return JsonResponse({'data': 'Membresia eliminada'}, safe=False)
    return JsonResponse({'data': 'No se encontró el id'}, safe=False)


@csrf_exempt
def medidas(request, id):
    if request.method == 'GET':
        medidas = list(Medidas.objects.filter(id=id).values())
        if medidas:
            logger.info("Se obtuvo las medidas con id: " + str(id))
            return JsonResponse({'data': medidas}, safe=False)
        else:
            logger.error("No se encontró las medidas con id: " + str(id))
            return JsonResponse({'data': 'No se encontró el id'}, safe=False)
        return JsonResponse({'data': medidas}, safe=False)
    elif request.method == 'POST':
        data = json.loads(request.body)
        medidas = Medidas.objects.create(**data)
        logger.info("Se creo las medidas con id: " + str(id))
        return JsonResponse({'data': 'Medidas creadas'}, safe=False)
    elif request.method == 'PUT':
        data = json.loads(request.body)
        medidas = Medidas.objects.filter(id=id).update(**data)
        logger.info("Se actualizo las medidas con id: " + str(id))
        return JsonResponse({'data': 'Medidas actualizadas'}, safe=False)
    elif request.method == 'DELETE':
        medidas = Medidas.objects.filter(id=id)
        if medidas:
            medidas.delete()
            logger.info("Se elimino las medidas con id: " + str(id))
            return JsonResponse({'data': 'Medidas eliminadas'}, safe=False)
        else:
            logger.error("No se encontró las medidas con id: " + str(id))
            return JsonResponse({'data': 'No se encontró el id'}, safe=False)
        return JsonResponse({'data': 'Medidas eliminadas'}, safe=False)
    return JsonResponse({'data': 'No se encontró el id'}, safe=False)


@csrf_exempt
def tiposMembresias(request, id):
    if request.method == 'GET':
        tiposMembresias = list(TipoMembresia.objects.filter(id=id).values())
        if tiposMembresias:
            logger.info("Se obtuvo el tipo de membresia con id: " + str(id))
            return JsonResponse({'data': tiposMembresias}, safe=False)
        else:
            logger.error("No se encontró el tipo de membresia con id: " + str(id))
            return JsonResponse({'data': 'No se encontró el id'}, safe=False)
    elif request.method == 'POST':
        data = json.loads(request.body)
        tiposMembresias = TipoMembresia.objects.create(**data)
        logger.info("Se creo el tipo de membresia con id: " + str(id))
        return JsonResponse({'data': 'Tipo de membresia creada'}, safe=False)
    elif request.method == 'PUT':
        data = json.loads(request.body)
        tiposMembresias = TipoMembresia.objects.filter(id=id).update(**data)
        logger.info("Se actualizo el tipo de membresia con id: " + str(id))
        return JsonResponse({'data': 'Tipo de membresia actualizada'}, safe=False)
    elif request.method == 'DELETE':
        tiposMembresias = TipoMembresia.objects.filter(id=id)
        if tiposMembresias:
            tiposMembresias.delete()
            logger.info("Se elimino el tipo de membresia con id: " + str(id))
            return JsonResponse({'data': 'Tipo de membresia eliminada'}, safe=False)
        else:
            logger.error("No se encontró el tipo de membresia con id: " + str(id))
            return JsonResponse({'data': 'No se encontró el id'}, safe=False)
        return JsonResponse({'data': 'Tipo de membresia eliminada'}, safe=False)
    return JsonResponse({'data': 'No se encontró el id'}, safe=False)


@csrf_exempt
def cargo(request, id):
    if request.method == 'GET':
        cargos = list(Cargo.objects.filter(id=id).values())
        if cargos:
            logger.info("Se obtuvo el cargo con id: " + str(id))
            return JsonResponse({'data': cargos}, safe=False)
        else:
            logger.error("No se encontró el cargo con id: " + str(id))
            return JsonResponse({'data': 'No se encontró el id'}, safe=False)
    elif request.method == 'POST':
        data = json.loads(request.body)
        cargos = Cargo.objects.create(**data)
        logger.info("Se creo el cargo con id: " + str(id))
        return JsonResponse({'data': 'Cargo creado'}, safe=False)
    elif request.method == 'PUT':
        data = json.loads(request.body)
        cargos = Cargo.objects.filter(id=id).update(**data)
        logger.info("Se actualizo el cargo con id: " + str(id))
        return JsonResponse({'data': 'Cargo actualizado'}, safe=False)
    elif request.method == 'DELETE':
        cargos = Cargo.objects.filter(id=id)
        if cargos:
            cargos.delete()
            logger.info("Se elimino el cargo con id: " + str(id))
            return JsonResponse({'data': 'Cargo eliminado'}, safe=False)
        else:
            logger.error("No se encontró el cargo con id: " + str(id))
            return JsonResponse({'data': 'No se encontró el id'}, safe=False)
    return JsonResponse({'data': 'Cargo eliminado'}, safe=False)


@csrf_exempt
def asignacionRutina(request, id):
    if request.method == 'GET':
        asignacionRutinas = list(AsignacionRutina.objects.filter(id=id).values())
        if asignacionRutinas:
            logger.info("Se obtuvo la asignacion de rutina con id: " + str(id))
            return JsonResponse({'data': asignacionRutinas}, safe=False)
        else:
            logger.error("No se encontró la asignacion de rutina con id: " + str(id))
            return JsonResponse({'data': 'No se encontró el id'}, safe=False)
    elif request.method == 'POST':
        data = json.loads(request.body)
        asignacionRutinas = AsignacionRutina.objects.create(**data)
        logger.info("Se creo la asignacion de rutina con id: " + str(id))
        return JsonResponse({'data': 'Asignacion de rutina creada'}, safe=False)
    elif request.method == 'PUT':
        data = json.loads(request.body)
        asignacionRutinas = AsignacionRutina.objects.filter(id=id).update(**data)
        logger.info("Se actualizo la asignacion de rutina con id: " + str(id))
        return JsonResponse({'data': 'Asignacion de rutina actualizada'}, safe=False)
    elif request.method == 'DELETE':
        asignacionRutinas = AsignacionRutina.objects.filter(id=id)
        if asignacionRutinas:
            asignacionRutinas.delete()
            logger.info("Se elimino la asignacion de rutina con id: " + str(id))
            return JsonResponse({'data': 'Asignacion de rutina eliminada'}, safe=False)
        else:
            logger.error("No se encontró la asignacion de rutina con id: " + str(id))
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
                logger.error("Usuario bloqueado")
                return JsonResponse({'auth': False, 'error': 'Usuario bloqueado'}, safe=False)
            else:
                if check_password(clave, cliente.clave):
                    data = model_to_dict(cliente)
                    data['foto'] = str(data['foto'])
                    # log del usuario
                    logger.info("Usuario logeado: " + str(cliente.correo))
                    return JsonResponse([{'auth': True, 'data': data}], safe=False)
                else:
                    if cliente.intentos < 3:
                        cliente.intentos = cliente.intentos + 1
                        cliente.save()
                        logger.error("Usuario o Contraseña incorrecta" + str(cliente.correo))
                        return JsonResponse({'auth': False, 'error': 'Usuario o Contraseña incorrecta'}, safe=False)
                    elif cliente.intentos == 3:
                        cliente.bloqueado = True
                        cliente.save()
                        logger.error("Usuario bloqueado" + str(cliente.correo))
        return JsonResponse({'auth': False, 'error': 'Usuario bloqueado'}, safe=False)
    else:
        return JsonResponse({'auth': False, 'data': 'Usuario no encontrado'}, safe=False)


@csrf_exempt
def ejercicio(request, id):
    if request.method == 'GET':
        ejercicios = list(Ejercicio.objects.filter(id=id).values())
        if ejercicios:
            logger.info("Se obtuvo el ejercicio con id: " + str(id))
            return JsonResponse({'data': ejercicios}, safe=False)
        else:
            logger.error("No se encontró el ejercicio con id: " + str(id))
            return JsonResponse({'data': 'No se encontró el id'}, safe=False)
    elif request.method == 'POST':
        data = json.loads(request.body)
        ejercicios = Ejercicio.objects.create(**data)
        logger.info("Se creo el ejercicio con id: " + str(id))
        return JsonResponse({'data': 'Ejercicio creado'}, safe=False)
    elif request.method == 'PUT':
        data = json.loads(request.body)
        ejercicios = Ejercicio.objects.filter(id=id).update(**data)
        logger.info("Se actualizo el ejercicio con id: " + str(id))
        return JsonResponse({'data': 'Ejercicio actualizado'}, safe=False)
    elif request.method == 'DELETE':
        ejercicios = Ejercicio.objects.filter(id=id)
        if ejercicios:
            ejercicios.delete()
            logger.info("Se elimino el ejercicio con id: " + str(id))
            return JsonResponse({'data': 'Ejercicio eliminado'}, safe=False)
        else:
            logger.error("No se encontró el ejercicio con id: " + str(id))
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
                logger.error("Usuario bloqueado" + str(empleado.correo))
                return JsonResponse({'auth': False, 'error': 'Usuario bloqueado'}, safe=False)
            else:
                if check_password(clave, empleado.clave):
                    data = model_to_dict(empleado)
                    logger.info("Usuario logeado: " + str(empleado.correo))
                    return JsonResponse([{'auth': True, 'data': data}], safe=False)
                else:
                    if empleado.intentos < 3:
                        empleado.intentos = empleado.intentos + 1
                        empleado.save()
                        logger.error("Usuario o Contraseña incorrecta" + str(empleado.correo))
                        return JsonResponse({'auth': False, 'error': 'Usuario o Contraseña incorrecta'}, safe=False)
                    elif empleado.intentos == 3:
                        empleado.bloqueado = True
                        empleado.save()
                        logger.error("Usuario bloqueado" + str(empleado.correo))
        logger.error("Usuario bloqueado" + str(empleado.correo))
        return JsonResponse({'auth': False, 'error': 'Usuario bloqueado'}, safe=False)
    else:
        logger.error("Usuario no encontrado" )
        return JsonResponse({'auth': False, 'data': 'Usuario no encontrado'}, safe=False)


@csrf_exempt
def dieta(request, id):
    if request.method == 'GET':
        dietas = list(Dieta.objects.filter(id=id).values())
        if dietas:
            logger.info("Se obtuvo la dieta con id: " + str(id))
            return JsonResponse({'data': dietas}, safe=False)
        else:
            logger.error("No se encontró la dieta con id: " + str(id))
            return JsonResponse({'data': 'No se encontró el id'}, safe=False)
    elif request.method == 'POST':
        data = json.loads(request.body)
        dietas = Dieta.objects.create(**data)
        logger.info("Se creo la dieta con id: " + str(id))
        return JsonResponse({'data': 'Dieta creada'}, safe=False)
    elif request.method == 'PUT':
        data = json.loads(request.body)
        dietas = Dieta.objects.filter(id=id).update(**data)
        logger.info("Se actualizo la dieta con id: " + str(id))
        return JsonResponse({'data': 'Dieta actualizada'}, safe=False)
    elif request.method == 'DELETE':
        dietas = Dieta.objects.filter(id=id)
        if dietas:
            dietas.delete()
            logger.info("Se elimino la dieta con id: " + str(id))
        return JsonResponse({'data': 'Dieta eliminada'}, safe=False)
    else:
        logger.error("No se encontró la dieta con id: " + str(id))
        return JsonResponse({'data': 'No se encontró el id'}, safe=False)


@csrf_exempt
def parametrosFactura(request):

    if request.method == 'GET':
        # parametrosFacturas = ParametrosFactura.objects.latest('id')
        parametrosFacturas = ParametrosFactura.objects.filter(activo=True).first()


        if parametrosFacturas:
            if str(parametrosFacturas.ultimaFactura) == str(parametrosFacturas.rangoFinal):
                parametrosFacturas.activo = False
                logger.info("Cambio de rango de facturas" + str(parametrosFacturas.id))
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
                logger.info("Se creo el nuevo rango de facturas" + str(parametrosFacturas.id) + "desde " + str(parametrosFacturas.rangoInicial) + "hasta " + str(parametrosFacturas.rangoFinal))
                return JsonResponse({'data': model_to_dict(parametrosFacturas)}, safe=False)

            return JsonResponse({'data': model_to_dict(parametrosFacturas)}, safe=False)
        else:
            logger.error("No se encontró el id")
            return JsonResponse({'data': 'No se encontró el id'}, safe=False)
    elif request.method == 'POST':
        data = json.loads(request.body)
        parametrosFacturas = ParametrosFactura.objects.create(**data)
        logger.info("Se creo el nuevo rango de facturas" + str(parametrosFacturas.id) + "desde " + str(parametrosFacturas.rangoInicial) + "hasta " + str(parametrosFacturas.rangoFinal))
        return JsonResponse({'data': 'Parametros de factura creados'}, safe=False)
    elif request.method == 'PUT':
        data = json.loads(request.body)
        parametrosFacturas = ParametrosFactura.objects.filter(id=id).update(**data)
        logger.info("Se actualizo el rango de facturas" + str(parametrosFacturas.id) + "desde " + str(parametrosFacturas.rangoInicial) + "hasta " + str(parametrosFacturas.rangoFinal))
        return JsonResponse({'data': 'Parametros de factura actualizados'}, safe=False)
    elif request.method == 'DELETE':
        parametrosFacturas = ParametrosFactura.objects.filter(id=id)
        if parametrosFacturas:
            parametrosFacturas.delete()
            logger.info("Se elimino el rango de facturas" + str(parametrosFacturas.id) + "desde " + str(parametrosFacturas.rangoInicial) + "hasta " + str(parametrosFacturas.rangoFinal))
            return JsonResponse({'data': 'Parametros de factura eliminados'}, safe=False)
        else:
            logger.error("No se encontró el id")
            return JsonResponse({'data': 'No se encontró el id'}, safe=False)
    return JsonResponse({'data': 'Parametros de factura eliminados'}, safe=False)


@csrf_exempt
def empleadoCargo(request, id):
    if request.method == 'GET':
        empleadosCargos = list(EmpleadoCargo.objects.filter(id=id).values())
        if empleadosCargos:
            logger.info("Se obtuvo el empleadoCargo con id: " + str(id))
            return JsonResponse({'data': empleadosCargos}, safe=False)
        else:
            logger.error("No se encontró el id" + str(id))
            return JsonResponse({'data': 'No se encontró el id'}, safe=False)
    elif request.method == 'POST':
        data = json.loads(request.body)
        empleadosCargos = EmpleadoCargo.objects.create(**data)
        logger.info("Se creo el empleadoCargo con id: " + str(id))
        return JsonResponse({'data': 'EmpleadoCargo creado'}, safe=False)
    elif request.method == 'PUT':
        data = json.loads(request.body)
        empleadosCargos = EmpleadoCargo.objects.filter(id=id).update(**data)
        logger.info("Se actualizo el empleadoCargo con id: " + str(id))
        return JsonResponse({'data': 'EmpleadoCargo actualizado'}, safe=False)
    elif request.method == 'DELETE':
        empleadosCargos = EmpleadoCargo.objects.filter(id=id)
        if empleadosCargos:
            empleadosCargos.delete()
            logger.info("Se elimino el empleadoCargo con id: " + str(id))
            return JsonResponse({'data': 'EmpleadoCargo eliminado'}, safe=False)
        else:
            logger.error("No se encontró el id" + str(id))
            return JsonResponse({'data': 'No se encontró el id'}, safe=False)
    return JsonResponse({'data': 'EmpleadoCargo eliminado'}, safe=False)


@csrf_exempt
def detallePlanilla(request, id):
    if request.method == 'GET':
        detallesPlanillas = list(DetallePlanilla.objects.filter(id=id).values())
        if detallesPlanillas:
            logger.info("Se obtuvo el detallePlanilla con id: " + str(id))
            return JsonResponse({'data': detallesPlanillas}, safe=False)
        else:
            logger.error("No se encontró el id" + str(id))
            return JsonResponse({'data': 'No se encontró el id'}, safe=False)
    elif request.method == 'POST':
        data = json.loads(request.body)
        detallesPlanillas = DetallePlanilla.objects.create(**data)
        logger.info("Se creo el detallePlanilla con id: " + str(id))
        return JsonResponse({'data': 'DetallePlanilla creado'}, safe=False)
    elif request.method == 'PUT':
        data = json.loads(request.body)
        detallesPlanillas = DetallePlanilla.objects.filter(id=id).update(**data)
        logger.info("Se actualizo el detallePlanilla con id: " + str(id))
        return JsonResponse({'data': 'DetallePlanilla actualizado'}, safe=False)
    elif request.method == 'DELETE':
        detallesPlanillas = DetallePlanilla.objects.filter(id=id)
        if detallesPlanillas:
            detallesPlanillas.delete()
            logger.info("Se elimino el detallePlanilla con id: " + str(id))
            return JsonResponse({'data': 'DetallePlanilla eliminado'}, safe=False)
        else:
            logger.error("No se encontró el id" + str(id))
            return JsonResponse({'data': 'No se encontró el id'}, safe=False)
    return JsonResponse({'data': 'DetallePlanilla eliminado'}, safe=False)


@csrf_exempt
def planilla(request, id):
    if request.method == 'GET':
        planillas = list(Planilla.objects.filter(id=id).values())
        if planillas:
            logger.info("Se obtuvo la planilla con id: " + str(id))
            return JsonResponse({'data': planillas}, safe=False)
        else:
            logger.error("No se encontró el id" + str(id))
            return JsonResponse({'data': 'No se encontró el id'}, safe=False)
    elif request.method == 'POST':
        data = json.loads(request.body)
        planillas = Planilla.objects.create(**data)
        logger.info("Se creo la planilla con id: " + str(id))
        return JsonResponse({'data': 'Planilla creada'}, safe=False)
    elif request.method == 'PUT':
        data = json.loads(request.body)
        planillas = Planilla.objects.filter(id=id).update(**data)
        logger.info("Se actualizo la planilla con id: " + str(id))
        return JsonResponse({'data': 'Planilla actualizada'}, safe=False)
    elif request.method == 'DELETE':
        planillas = Planilla.objects.filter(id=id)
        if planillas:
            planillas.delete()
            logger.info("Se elimino la planilla con id: " + str(id))
            return JsonResponse({'data': 'Planilla eliminada'}, safe=False)
        else:
            logger.error("No se encontró el id" + str(id))
            return JsonResponse({'data': 'No se encontró el id'}, safe=False)
    return JsonResponse({'data': 'Planilla eliminada'}, safe=False)


@csrf_exempt
def membresiasClientes(request, id):
    if request.method == 'GET':
        membresiasCliente = Membresia.objects.filter(cliente=id).values()

        if len(membresiasCliente) <= 0:
            logger.error("No tiene suscripcion activa" + str(id))
            return JsonResponse({'data': 'No tienes suscripcion activa', "suscripcionActiva": False,}, safe=False)
        tipoMembresia = TipoMembresia.objects.filter(id=membresiasCliente[0]['tipoMembresia_id']).values()

        if membresiasCliente:
            membresiasCliente = membresiasCliente[0]
            membresiasCliente['NombreMembresia'] = tipoMembresia[0]['nombreMembresia']
            membresiasCliente['descripcionMembresia'] = tipoMembresia[0]['descripcion']
            membresiasCliente['precioMembresia'] = tipoMembresia[0]['precio']
            membresiasCliente['tiempoRestanteDias'] = (membresiasCliente['fechaFinal'] - datetime.now(timezone.utc)).days
            membresiasCliente['SuscripcionActiva'] = True
            logger.info("Se obtuvo la membresia del cliente con id: " + str(id))
            return JsonResponse(membresiasCliente, safe=False)
        else:
            logger.error("No se encontró el id" + str(id))
            return JsonResponse({'error': "No se encontro Cliente"})


@csrf_exempt
def actualizarUltimaFactura(request, id):
    if request.method == 'GET':
        parametrosFactura = ParametrosFactura.objects.latest('id')
        if parametrosFactura:
            parametrosFactura.ultimaFactura = parametrosFactura.ultimaFactura + 1
            parametrosFactura.save()
            logger.info("Se actualizo la ultima factura")
            return JsonResponse({'data': "Ultima factura actualizada"}, safe=False)

        else:
            logger.error("No se encontró el id" + str(id))
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
            logger.info("Factura encontrada")
            return JsonResponse({'data': factura}, safe=False)
        else:
            logger.error("No se encontró el id" + str(id))
            return JsonResponse({'data': 'No se encontró el id'}, safe=False)
    return JsonResponse({'data': 'No se encontró el id'}, safe=False)


@csrf_exempt
def getFacturaByCliente(request, id):
    if request.method == 'GET':
        factura = list(Factura.objects.filter(cliente=id).order_by('-id').values())
        if factura:
            logger.info("Se encotro factura con id" + str(id) )
            return JsonResponse({'data': factura}, safe=False)
        else:
            logger.error("No se encontro el id " + str(id))
            return JsonResponse({'data': 'No se encontró el id'}, safe=False)
        if factura:
            logger.info("Factura encontrada" + str(id))
            return JsonResponse({'data': factura}, safe=False)
        else:
            logger.error("No se encontró el id" + str(id))
            return JsonResponse({'data': 'No se encontró el id'}, safe=False)
    return JsonResponse({'data': 'No se encontró el id'}, safe=False)

@csrf_exempt
def getRutinasByCliente(request, id):
    if request.method == 'GET':
        rutinas = list(Rutina.objects.filter(cliente=id).values())
        if rutinas:
            logger.info("Se encotro rutina con id" + str(id) )
            return JsonResponse({'data': rutinas}, safe=False)
        else:
            logger.error("No se encontro el id " + str(id))
            return JsonResponse({'data': 'No se encontró el id'}, safe=False)
    return JsonResponse({'data': 'No se encontró el id'}, safe=False)

@csrf_exempt
def getDietasByCliente(request, id):
    if request.method == 'GET':
        dietas = list(Dieta.objects.filter(cliente=id).values())
        if dietas:
            logger.info("Se encotro dieta con id" + str(id) )
            return JsonResponse({'data': dietas}, safe=False)
        else:
            logger.error("No se encontro el id " + str(id))
            return JsonResponse({'data': 'No se encontró el id'}, safe=False)
    return JsonResponse({'data': 'No se encontró el id'}, safe=False)

@csrf_exempt
def getAsignacionClaseByCliente(request, id):
    if request.method == 'GET':
        asignacionClase = list(AsignacionClase.objects.filter(cliente=id).values())
        if asignacionClase:
            logger.info("Se encotro asignacion de clase con id" + str(id) )
            return JsonResponse({'data': asignacionClase}, safe=False)
        else:
            logger.error("No se encontro el id " + str(id))
            return JsonResponse({'data': 'No se encontró el id'}, safe=False)
    return JsonResponse({'data': 'No se encontró el id'}, safe=False)

@csrf_exempt
def getMedidasByCliente(request, id):
    if request.method == 'GET':
        medidas = list(Medidas.objects.filter(cliente=id).values())
        if medidas:
            logger.info("Se encotro medidas con id" + str(id) )
            return JsonResponse({'data': medidas}, safe=False)
        else:
            logger.error("No se encontro el id " + str(id))
            return JsonResponse({'data': 'No se encontró el id'}, safe=False)
    return JsonResponse({'data': 'No se encontró el id'}, safe=False)

@csrf_exempt
def exportEmpleadosCSV(request):
    if request.method == "GET":
        response = generar_csv(request, 'Empleado')
        logger.info("Se exporto el archivo csv de empleados")
        return response
    
@csrf_exempt
def exportEmpleadosPDF(request):
    if request.method == "GET":
        response = generar_pdf(request, 'Empleado')
        logger.info("Se exporto el archivo pdf de empleados")
        return response
    
@csrf_exempt
def exportTiposMembresiaCSV(request):
    if request.method == "GET":
        response = generar_csv(request, 'TipoMembresia')
        logger.info("Se exporto el archivo csv de tipos de membresia")
        return response
    
@csrf_exempt
def exportTiposMembresiaPDF(request):
    if request.method == "GET":
        response = generar_pdf(request, 'TipoMembresia')
        logger.info("Se exporto el archivo pdf de tipos de membresia")
        return response
    
@csrf_exempt
def exportPreciosHistoricoMembresiaCSV(request):
    if request.method == "GET":
        response = generar_csv(request, 'PrecioHistoricoMembresia')
        logger.info("Se exporto el archivo csv de precios historicos de membresia")
        return response
    
@csrf_exempt
def exportPreciosHistoricoMembresiaPDF(request):
    if request.method == "GET":
        response = generar_pdf(request, 'PrecioHistoricoMembresia')
        logger.info("Se exporto el archivo pdf de precios historicos de membresia")
        return response
    
@csrf_exempt
def exportTiposDocumentoClienteCSV(request):
    if request.method == "GET":
        response = generar_csv(request, 'TipoDocumentoCliente')
        logger.info("Se exporto el archivo csv de tipos de documento de cliente")
        return response
    
@csrf_exempt
def exportTiposDocumentoClientePDF(request):
    if request.method == "GET":
        response = generar_pdf(request, 'TipoDocumentoCliente')
        logger.info("Se exporto el archivo pdf de tipos de documento de cliente")
        return response
    
@csrf_exempt
def exportTiposSangreClienteCSV(request):
    if request.method == "GET":
        response = generar_csv(request, 'TipoSangreCliente')
        logger.info("Se exporto el archivo csv de tipos de sangre de cliente")
        return response
    
@csrf_exempt
def exportTiposSangreClientePDF(request):
    if request.method == "GET":
        response = generar_pdf(request, 'TipoSangreCliente')
        logger.info("Se exporto el archivo pdf de tipos de sangre de cliente")
        return response
    
@csrf_exempt
def exportClientesCSV(request):
    if request.method == "GET":
        response = generar_csv(request, 'Cliente')
        logger.info("Se exporto el archivo csv de clientes")
        return response
    
@csrf_exempt
def exportClientesPDF(request):
    if request.method == "GET":
        response = generar_pdf(request, 'Cliente')
        logger.info("Se exporto el archivo pdf de clientes")
        return response
    
@csrf_exempt
def exportCuponesCSV(request):
    if request.method == "GET":
        response = generar_csv(request, 'Cupon')
        logger.info("Se exporto el archivo csv de cupones")
        return response
    
@csrf_exempt
def exportCuponesPDF(request):
    if request.method == "GET":
        response = generar_pdf(request, 'Cupon')
        logger.info("Se exporto el archivo pdf de cupones")
        return response
    
@csrf_exempt
def exportDescuentosCSV(request):
    if request.method == "GET":
        response = generar_csv(request, 'Descuento')
        logger.info("Se exporto el archivo csv de descuentos")
        return response
    
@csrf_exempt
def exportDescuentosPDF(request):
    if request.method == "GET":
        response = generar_pdf(request, 'Descuento')
        logger.info("Se exporto el archivo pdf de descuentos")
        return response
    
@csrf_exempt
def exportMembresiasCSV(request):
    if request.method == "GET":
        response = generar_csv(request, 'Membresia')
        logger.info("Se exporto el archivo csv de membresias")
        return response
    
@csrf_exempt
def exportMembresiasPDF(request):
    if request.method == "GET":
        response = generar_pdf(request, 'Membresia')
        logger.info("Se exporto el archivo pdf de membresias")
        return response
    
@csrf_exempt
def exportEjerciciosCSV(request):
    if request.method == "GET":
        response = generar_csv(request, 'Ejercicio')
        logger.info("Se exporto el archivo csv de ejercicios")
        return response
    
@csrf_exempt
def exportEjerciciosPDF(request):
    if request.method == "GET":
        response = generar_pdf(request, 'Ejercicio')
        logger.info("Se exporto el archivo pdf de ejercicios")
        return response
    
@csrf_exempt
def exportMusculosCSV(request):
    if request.method == "GET":
        response = generar_csv(request, 'Musculo')
        logger.info("Se exporto el archivo csv de musculos")
        return response
    
@csrf_exempt
def exportMusculosPDF(request):
    if request.method == "GET":
        response = generar_pdf(request, 'Musculo')
        logger.info("Se exporto el archivo pdf de musculos")
        return response
    
@csrf_exempt
def exportMusculosEjerciciosCSV(request):
    if request.method == "GET":
        response = generar_csv(request, 'MusculoEjercicio')
        logger.info("Se exporto el archivo csv de musculos ejercicios")
        return response
    
@csrf_exempt
def exportMusculosEjerciciosPDF(request):
    if request.method == "GET":
        response = generar_pdf(request, 'MusculoEjercicio')
        logger.info("Se exporto el archivo pdf de musculos ejercicios")
        return response
    
@csrf_exempt
def exportAsignacionesRutinaCSV(request):
    if request.method == "GET":
        response = generar_csv(request, 'AsignacionRutina')
        logger.info("Se exporto el archivo csv de asignaciones de rutina")
        return response
    
@csrf_exempt
def exportAsignacionesRutinaPDF(request):
    if request.method == "GET":
        response = generar_pdf(request, 'AsignacionRutina')
        logger.info("Se exporto el archivo pdf de asignaciones de rutina")
        return response
    
@csrf_exempt
def exportRutinasCSV(request):
    if request.method == "GET":
        response = generar_csv(request, 'Rutina')
        logger.info("Se exporto el archivo csv de rutinas")
        return response
    
@csrf_exempt
def exportRutinasPDF(request):
    if request.method == "GET":
        response = generar_pdf(request, 'Rutina')
        logger.info("Se exporto el archivo pdf de rutinas")
        return response
    
@csrf_exempt
def exportComidasCSV(request):
    if request.method == "GET":
        response = generar_csv(request, 'Comida')
        logger.info("Se exporto el archivo csv de comidas")
        return response
    
@csrf_exempt
def exportComidasPDF(request):
    if request.method == "GET":
        response = generar_pdf(request, 'Comida')
        logger.info("Se exporto el archivo pdf de comidas")
        return response
    
@csrf_exempt
def exportAsignacionesDietaCSV(request):
    if request.method == "GET":
        response = generar_csv(request, 'AsignacionDieta')
        logger.info("Se exporto el archivo csv de asignaciones de dieta")
        return response
    
@csrf_exempt
def exportAsignacionesDietaPDF(request):
    if request.method == "GET":
        response = generar_pdf(request, 'AsignacionDieta')
        logger.info("Se exporto el archivo pdf de asignaciones de dieta")
        return response
    
@csrf_exempt
def exportDietasCSV(request):
    if request.method == "GET":
        response = generar_csv(request, 'Dieta')
        logger.info("Se exporto el archivo csv de dietas")
        return response
    
@csrf_exempt
def exportDietasPDF(request):
    if request.method == "GET":
        response = generar_pdf(request, 'Dieta')
        logger.info("Se exporto el archivo pdf de dietas")
        return response
    
@csrf_exempt
def exportMedidasCSV(request):
    if request.method == "GET":
        response = generar_csv(request, 'Medida')
        logger.info("Se exporto el archivo csv de medidas")
        return response
    
@csrf_exempt
def exportMedidasPDF(request):
    if request.method == "GET":
        response = generar_pdf(request, 'Medida')
        logger.info("Se exporto el archivo pdf de medidas")
        return response
    
@csrf_exempt
def exportLogClientesCSV(request):
    if request.method == "GET":
        response = generar_csv(request, 'LogCliente')
        logger.info("Se exporto el archivo csv de log de clientes")
        return response
    
@csrf_exempt
def exportLogClientesPDF(request):
    if request.method == "GET":
        response = generar_pdf(request, 'LogCliente')
        logger.info("Se exporto el archivo pdf de log de clientes")
        return response
    
@csrf_exempt
def exportTiposGeneroCSV(request):
    if request.method == "GET":
        response = generar_csv(request, 'TipoGenero')
        logger.info("Se exporto el archivo csv de tipos de genero")
        return response
    
@csrf_exempt
def exportTiposGeneroPDF(request):
    if request.method == "GET":
        response = generar_pdf(request, 'TipoGenero')
        logger.info("Se exporto el archivo pdf de tipos de genero")
        return response
    
@csrf_exempt
def exportDocumentosEmpleadoCSV(request):
    if request.method == "GET":
        response = generar_csv(request, 'DocumentoEmpleado')
        logger.info("Se exporto el archivo csv de documentos de empleado")
        return response
    
@csrf_exempt
def exportDocumentosEmpleadoPDF(request):
    if request.method == "GET":
        response = generar_pdf(request, 'DocumentoEmpleado')
        logger.info("Se exporto el archivo pdf de documentos de empleado")
        return response
    
@csrf_exempt
def exportCargosCSV(request):
    if request.method == "GET":
        response = generar_csv(request, 'Cargo')
        logger.info("Se exporto el archivo csv de cargos")
        return response
    
@csrf_exempt
def exportCargosPDF(request):
    if request.method == "GET":
        response = generar_pdf(request, 'Cargo')
        logger.info("Se exporto el archivo pdf de cargos")
        return response
    
@csrf_exempt
def exportEmpleadosCargoCSV(request):
    if request.method == "GET":
        response = generar_csv(request, 'EmpleadoCargo')
        logger.info("Se exporto el archivo csv de empleados por cargo")
        return response
    
@csrf_exempt
def exportEmpleadosCargoPDF(request):
    if request.method == "GET":
        response = generar_pdf(request, 'EmpleadoCargo')
        logger.info("Se exporto el archivo pdf de empleados por cargo")
        return response
    
@csrf_exempt
def exportDetallesPlanillaCSV(request):
    if request.method == "GET":
        response = generar_csv(request, 'DetallePlanilla')
        logger.info("Se exporto el archivo csv de detalles de planilla")
        return response
    
@csrf_exempt
def exportDetallesPlanillaPDF(request):
    if request.method == "GET":
        response = generar_pdf(request, 'DetallePlanilla')
        logger.info("Se exporto el archivo pdf de detalles de planilla")
        return response
    
@csrf_exempt
def exportPlanillasCSV(request):
    if request.method == "GET":
        response = generar_csv(request, 'Planilla')
        logger.info("Se exporto el archivo csv de planillas")
        return response
    
@csrf_exempt
def exportPlanillasPDF(request):
    if request.method == "GET":
        response = generar_pdf(request, 'Planilla')
        logger.info("Se exporto el archivo pdf de planillas")
        return response
    
@csrf_exempt
def exportFacturasCSV(request):
    if request.method == "GET":
        response = generar_csv(request, 'Factura')
        logger.info("Se exporto el archivo csv de facturas")
        return response
    
@csrf_exempt
def exportFacturasPDF(request):
    if request.method == "GET":
        response = generar_pdf(request, 'Factura')
        logger.info("Se exporto el archivo pdf de facturas")
        return response
    
@csrf_exempt
def exportParametrosFacturasCSV(request):
    if request.method == "GET":
        response = generar_csv(request, 'ParametrosFactura')
        logger.info("Se exporto el archivo csv de parametros de facturas")
        return response
    
@csrf_exempt
def exportParametrosFacturasPDF(request):
    if request.method == "GET":
        response = generar_pdf(request, 'ParametrosFactura')
        logger.info("Se exporto el archivo pdf de parametros de facturas")
        return response