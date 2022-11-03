from django.contrib import admin
from .models import *


# Register your models here.


admin.site.register(TipoMembresia)
admin.site.register(Cliente)
admin.site.register(TipoDocumentoCliente)
admin.site.register(TipoGeneroCliente)
admin.site.register(TipoSangreCliente)
admin.site.register(Medidas)

