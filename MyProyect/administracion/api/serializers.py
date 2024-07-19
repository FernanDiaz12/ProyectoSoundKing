from rest_framework.serializers import ModelSerializer
from administracion.models import Instrumentos

class InstrumentosSerializer(ModelSerializer):
    class Meta:
        model = Instrumentos
        fields = ['id', 'tipo_instrumento', 'material', 'marca', 'nombre', 'imagen', 'color', 'precio', 'peso', 'descripcion']