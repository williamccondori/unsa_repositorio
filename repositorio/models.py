from django.db import models

# Create your models here.


class Autor(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    dina = models.CharField(max_length=300)
    web = models.CharField(max_length=300)

class Documento(models.Model):
    titulo = models.CharField(max_length=300)
    anio = models.IntegerField()
    resumen = models.TextField()
    url = models.CharField(max_length=300)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    
class Puntuacion(models.Model):
    Documento = models.ForeignKey(Documento, on_delete=models.CASCADE)