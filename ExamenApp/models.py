from django.db import models

# Create your models here.

class Cliente(models.Model):
    rut_cli = models.CharField(primary_key=True, max_length=10)
    nombre_cli = models.CharField(max_length=50)
    apellido_cli = models.CharField(max_length=50)
    correo_cli = models.EmailField(max_length=254)
    contraseña_cli = models.CharField(max_length=50)

class Producto(models.Model):
    id_producto = models.IntegerField(primary_key=True)
    nombre_prod = models.CharField(max_length=50)
    precio_prod = models.IntegerField()
    imagem_prod = models.ImageField()
