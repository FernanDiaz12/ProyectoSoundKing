from django.db import models

# Create your models here.
class Marca(models.Model):
    id = models.IntegerField
    marca = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=200)

class Tipo_Instrumento(models.Model):
    id = models.IntegerField 
    tipo_instrumento = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=200)

class Material(models.Model):
    id = models.IntegerField 
    material = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=200) 

class Instrumentos(models.Model):
    id = models.IntegerField 
    tipo_instrumento = models.ForeignKey(Tipo_Instrumento,on_delete=models.CASCADE)
    material = models.ForeignKey(Material,on_delete=models.CASCADE)
    marca = models.ForeignKey(Marca,on_delete=models.CASCADE)
    nombre = models.CharField(max_length=50)
    imagen = models.CharField(max_length=200)
    color = models.CharField(max_length=20)
    precio = models.IntegerField
    peso = models.IntegerField
    descripcion = models.CharField(max_length=200)           

