from django.contrib import admin
from .models import  Marca
from .models import  Material
from .models import  Instrumentos
from .models import  Tipo_Instrumento

# Register your models here.

admin.site.register(Marca)
admin.site.register(Material)
admin.site.register(Instrumentos)
admin.site.register(Tipo_Instrumento)