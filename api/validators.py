from django.core.exceptions import ValidationError
from datetime import datetime,date

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