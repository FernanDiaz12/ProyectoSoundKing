from rest_framework.routers import DefaultRouter
from administracion.api.views import InstrumentosApiViewSet

router_administracion = DefaultRouter()

router_administracion.register(prefix='instrumentos', basename='instrumentos', viewset=InstrumentosApiViewSet)