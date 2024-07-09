from django.http import HttpResponse
from django.shortcuts import render

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
