from django.db import models

# Create your models here.


class Cliente(models.Model):
    nombre = models.CharField(max_length=240)
    apellido = models.CharField(max_length=240)
    telefono = models.CharField(max_length=240)
    dni = models.IntegerField(default=0)
    email = models.EmailField(max_length=240)
    empresa = models.CharField(max_length=240)


class Personal(models.Model):
    nombre = models.CharField(max_length=240)
    apellido = models.CharField(max_length=240)
    telefono = models.CharField(max_length=240)
    dni = models.IntegerField(default=0)
    email = models.EmailField(max_length=240)
    sector = models.CharField(max_length=240)


class Producto(models.Model):
    marca = models.CharField(max_length=240)
    modelo = models.CharField(max_length=240)
    proveedor = models.CharField(max_length=240)
