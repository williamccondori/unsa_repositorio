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


class TipoCliente(models.Model):
    id = models.CharField(max_length=2, primary_key=True)
    nombre = models.CharField(max_length=50)


class Cliente(models.Model):
    ip_usuario = models.CharField(max_length=32)
    id_usuario = models.CharField(max_length=32)
    tipo_cliente = models.ForeignKey(
        TipoCliente, on_delete=models.CASCADE)


class Puntuacion(models.Model):
    documento = models.ForeignKey(Documento, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
