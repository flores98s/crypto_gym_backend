from rest_framework import routers
from .api import *


router = routers.DefaultRouter()

router.register('tiposmembresias',TipoMembresiaViewSet,'tiposmembresias')
router.register('cliente',ClienteViewSet,'clientes')

urlpatterns = router.urls