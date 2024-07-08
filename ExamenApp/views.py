from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, "Inicio.html")

def Login(request):
    return render(request, "Login.html")

