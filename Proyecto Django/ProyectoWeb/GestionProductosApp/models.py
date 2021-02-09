from django.db import models

# Create your models here.
class Producto(models.Model):
    nombre=models.CharField(max_length=50)
    precio=models.FloatField()
    seccion=models.CharField(max_length=50)
    descripcion=models.CharField(max_length=256)
    imgUrl=models.CharField(max_length=256)
    creado=models.DateTimeField(auto_now_add=True)
    actualizado=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.nombre