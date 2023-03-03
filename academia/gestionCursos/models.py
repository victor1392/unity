from django.db import models

# Create your models here.

class Alumnos(models.Model):
    nombre = models.CharField(max_length=30)
    direc = models.CharField(max_length=40)
    telefono = models.CharField(max_length=30)
    mail = models.EmailField()

class Cursos(models.Model):
    nombre = models.CharField(max_length=30)
    rama = models.CharField(max_length=30)
    pvp = models.FloatField()

class Pedido(models.Model):
    ref = models.IntegerField()
    fecha = models.DateField()
    finalizado = models.BooleanField()
