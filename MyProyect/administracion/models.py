from django.db import models

# Create your models here.
class Marca(models.Model):
    id = models.IntegerField
    marca = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=200)

    def __str__(self):
        return self.marca

class Tipo_Instrumento(models.Model):
    id = models.IntegerField 
    tipo_instrumento = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=200)

    def __str__(self):
        return self.tipo_instrumento

class Material(models.Model):
    id = models.IntegerField 
    material = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=200)
    
    def __str__(self):
        return self.material

class Instrumentos(models.Model):
    id = models.IntegerField(primary_key=True)
    tipo_instrumento = models.ForeignKey(Tipo_Instrumento,on_delete=models.CASCADE)
    material = models.ForeignKey(Material,on_delete=models.CASCADE)
    marca = models.ForeignKey(Marca,on_delete=models.CASCADE)
    nombre = models.CharField(max_length=50)
    imagen = models.CharField(max_length=200)
    color = models.CharField(max_length=20)
    precio = models.FloatField()
    peso = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre        

