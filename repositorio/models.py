from django.db import models


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


class ClienteWeb(models.Model):
    Ip = models.CharField(max_length=32)


class ClienteBot(models.Model):
    Id = models.CharField(max_length=32)


class TipoPuntuacion(models.Model):
    id = models.CharField(max_length=2)
    nombre = models.CharField(max_length=50)


class Puntuacion(models.Model):
    documento = models.ForeignKey(Documento, on_delete=models.CASCADE)
    tipo_puntuacion = models.ForeignKey(
        TipoPuntuacion, on_delete=models.CASCADE)
    cliente_web = models.ForeignKey(
        ClienteWeb, on_delete=models.CASCADE, blank=True, null=True)
    cliente_bot = models.ForeignKey(
        ClienteBot, on_delete=models.CASCADE, blank=True, null=True)
