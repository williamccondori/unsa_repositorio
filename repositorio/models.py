from django.db import models

# Create your models here.

<<<<<<< HEAD

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
=======
class Facultad(models.Model):
    nombre = models.CharField(max_length=200)


class Escuela(models.Model):
    nombre = models.CharField(max_length=200)
    facultad = models.ForeignKey(Facultad, on_delete=models.CASCADE)

class Asignatura(models.Model):
    nombre = models.CharField(max_length=200)
    escuela = models.ForeignKey(Escuela, on_delete=models.CASCADE)

class Categoria(models.Model):
    nombre = models.CharField(max_length=200)

class Autor(models.Model):
    nombre = models.CharField(max_length=200)
    apellido = models.CharField(max_length=200)

class TrabajoCurso(models.Model):
    titulo = models.CharField(max_length=200)
    resumen = models.TextField
    url = models.CharField(max_length=300)
    autor = models.ForeignKey(Asignatura, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
>>>>>>> 14cffe540bab930b2caa19348e8cea4a5b5af04c
