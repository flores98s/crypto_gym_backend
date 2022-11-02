from rest_framework import routers
from .api import TipoMembresiaViewSet


router = routers.DefaultRouter()

router.register('tiposmembresias',TipoMembresiaViewSet,'tiposmembresias')


urlpatterns = router.urls