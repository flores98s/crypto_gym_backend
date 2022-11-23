from django.shortcuts import render
from .models import *
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


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
            cliente.nombre = data['nombre']
            cliente.apellido = data['apellido']
            cliente.save()
            return JsonResponse({'data': 'Cliente actualizado'}, safe=False)
        else:
            return JsonResponse({'data': 'No se encontró el id'}, safe=False)
    return JsonResponse({'data': 'No se encontró el id'}, safe=False)



def rutina(request):
    if request.method == 'GET':
        rutinas = list(Rutina.objects.all().values())
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
def loginEmpleado(request):
    data = json.loads(request.body)
    correo = data['correo']
    clave = data['clave']

    if request.method == 'POST':
        empleado = Empleado.objects.filter(correo=correo, clave=clave).first()
        if empleado:
            return JsonResponse({'auth': True, 'data': empleado}, safe=False)
        else:
            return JsonResponse({'auth': False}, safe=False)

