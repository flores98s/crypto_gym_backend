from django.core.exceptions import ValidationError
from datetime import datetime,date
import re

def validate_fecha(value):
    print(value)
    if value >= date.today():
        raise ValidationError(
            (f'La fecha no puede ser mayor {date.today()}'),
        )

def validate_peso(value):
    if value < 50:
        raise ValidationError(
            (f'El peso no puede ser menor a 50 kg'),
        )

def validate_nombre(value):
    '''validar que no tenga símbolos'''
    if not re.match("^[a-zA-Z]*$", value):
        raise ValidationError(
            (f'El nombre no puede tener símbolos o números'),
        )

def validate_mayordedieciochoaños(value):
        #Dias en 18 años
        veintiunAñosEnDias = 365.2425 * 18
        hoy = date.today() 
        diferenciaDias =  hoy - value
        if  value >= hoy:
            raise ValidationError("La fecha de nacimiento no puede ser mayor o igual a la fecha de hoy")
        
        if diferenciaDias.days < veintiunAñosEnDias:
            raise ValidationError("El cliente no puede tener menos de 18 años")

def validate_mayordeveintiuno(value):
        #Dias en 21 años
        veintiunAñosEnDias = 365.2425 * 21
        hoy = date.today() 
        diferenciaDias =  hoy - value
        if  value >= hoy:
            raise ValidationError("La fecha de nacimiento no puede ser mayor o igual a la fecha de hoy")
        
        if diferenciaDias.days < veintiunAñosEnDias:
            raise ValidationError("El empleado no puede tener menos de 21 años")

def validate_numerotelefono(value):
    if not re.match("^[9|3|8][1-9]{7}", value):
        raise ValidationError(
            (f'El número de teléfono debe empezar con 3, 8 o 9'),
        )
