from django.shortcuts import render
from .models import Empleado, Cliente
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

def get_empleado(request, id):
    empleados = list(Empleado.objects.filter(id=id).values())
    return JsonResponse(empleados, safe=False)

def get_cliente(request, id):
    clientes = list(Cliente.objects.filter(id=id).values())
    return JsonResponse(clientes, safe=False)
    

@csrf_exempt
def loginEmpleado(request):
    data = json.loads(request.body)
    correo = data['correo']
    clave = data['clave']

    if request.method == 'POST':
        empleado = Empleado.objects.filter(correo=correo, clave=clave).first()
        if empleado:
            return JsonResponse({'auth':True,'data':empleado }, safe=False)
        else:
            return JsonResponse({'auth':False}, safe=False)