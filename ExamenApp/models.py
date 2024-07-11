from django.db import models

# Create your models here.

class Cliente(models.Model):
    rut_cli = models.CharField(primary_key=True, max_length=10)
    nombre_cli = models.CharField(max_length=50)
    apellido_cli = models.CharField(max_length=50)
    correo_cli = models.EmailField(max_length=254)
    contraseña_cli = models.CharField(max_length=50)
    def __str__(self):
        texto = "{0} ({1})"
        return texto.format(self.rut_cli,self.nombre_cli)

class Producto(models.Model):
    id_producto = models.PositiveSmallIntegerField(primary_key=True)
    nombre_prod = models.CharField(max_length=100)
    precio_prod = models.IntegerField()
    idioma_prod = models.CharField(max_length=25)

class DetalleVenta(models.Model):
    id_producto = models.PositiveSmallIntegerField()
    id_carrito = models.PositiveSmallIntegerField()
    nombre_prod = models.CharField(max_length=100)
    cantidad_prod = models.PositiveSmallIntegerField()
    precio_prod = models.IntegerField()

class Carrito(models.Model):
    id_carrito = models.PositiveSmallIntegerField()
    total_precio = models.IntegerField()
    
