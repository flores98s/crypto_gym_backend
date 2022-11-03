from rest_framework import routers
from .api import *


router = routers.DefaultRouter()

# url tiposmembresias
router.register('tiposmembresias',TipoMembresiaViewSet,'tiposmembresias')
# url cliente
router.register('cliente',ClienteViewSet,'clientes')
# url tipodocumentocliente
router.register('tipodocumentocliente',TipoDocumentoClienteViewSet,'tipodocumentoclientes')
# url tipogenerocliente
router.register('tipogenerocliente',TipoGeneroClienteViewSet,'tipogeneroclientes')
# url tiposangrecliente
router.register('tiposangrecliente',TipoSangreClienteViewSet,'tiposangreclientes')
# url medidas
router.register('medidas',MedidasViewSet,'medidas')


urlpatterns = router.urls