from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('CarritoDeCompras/', views.CarritoDeCompras),
    path('Tienda/', views.Tienda),
    path('registro/', views.registro),
    path('Tienda/', views.anadir_carrito)
]