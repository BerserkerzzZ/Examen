from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Cliente
from .models import Producto, DetalleVenta, Carrito
from .forms import CrearUsuarios
from django.contrib import messages
from django.contrib.auth import authenticate, login
# Create your views here.

def home(request):
    return render(request, "app/Inicio.html")

def CarritoDeCompras(request):
    return render(request, "app/CarritoDeCompras.html")

def Tienda(request):
    producto = Producto.objects.all()
    return render(request, "app/Tienda.html", {"Producto":producto})

def registro(request):
    data = {
        'form': CrearUsuarios()
    }

    if request.method == 'POST':
        formulario = CrearUsuarios(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
            login(request, user)
            messages.success(request,"Te has registrado correctamente.")
            return redirect(to="http://127.0.0.1:8000")
        data["form"] = formulario

    return render(request, 'registration/registro.html', data)

def det_venta(request):
    detalleVentas = DetalleVenta.objects.all()
    return render (request, "CarritoDeCompras.html", {"detalleVentas":detalleVentas})

def anadir_carrito(request):
    id_producto=request.POST['id_producto']
    nombre_prod=request.POST['nombre_prod']
    precio_prod=request.POST['precio_prod']

    detalleVenta=DetalleVenta.objects.create(id_producto=id_producto,nombre_prod=nombre_prod,precio_prod=precio_prod)
    messages.success(request,"Se añadio correctamente.")