from django.db import OperationalError
import logging

logger = logging.getLogger(__name__)

class DatabaseTimeoutMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        try:
            response = self.get_response(request)
        except OperationalError as e:
            logger.error('La conexión a la base de datos ha agotado el tiempo de espera: %s', str(e))
            # Realiza cualquier otra acción que desees, como enviar una alerta por correo electrónico o guardar en un archivo de registro.
            response = None
        return response
