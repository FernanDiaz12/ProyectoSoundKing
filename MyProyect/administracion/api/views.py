from rest_framework.viewsets import ModelViewSet
from administracion.models import Instrumentos
from administracion.api.serializers import InstrumentosSerializer

class InstrumentosApiViewSet(ModelViewSet):
    serializer_class = InstrumentosSerializer
    queryset = Instrumentos.objects.all()