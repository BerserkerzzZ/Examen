from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Cliente

# Create your views here.

def home(request):
    return render(request, "Inicio.html")

def Login(request):
    return render(request, "Login.html")

def CarritoDeCompras(request):
    return render(request, "CarritoDeCompras.html")

def Tienda(request):
    return render(request, "Tienda.html")

def CrearUsuario(request):
    return render(request, "CrearUsuario.html")

def CrearCliente(request):
    rut_cli=request.POST['rut_cli']
    nombre_cli=request.POST['nombre_cli']
    apellido_cli=request.POST['apellido_cli']
    correo_cli=request.POST['correo_cli']
    contraseña_cli=request.POST['contraseña_cli']

    cliente = Cliente.objects.create(
        rut_cli=rut_cli, nombre_cli=nombre_cli,apellido_cli=apellido_cli,correo_cli=correo_cli,contraseña_cli=contraseña_cli
    )
    return render(request, "Login.html")
