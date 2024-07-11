from django.contrib import admin
from .models import Cliente, Producto, DetalleVenta, Carrito

# Register your models here.

admin.site.register(Cliente)
admin.site.register(Producto)
admin.site.register(DetalleVenta)
admin.site.register(Carrito)