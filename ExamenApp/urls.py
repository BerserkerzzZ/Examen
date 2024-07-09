from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('Login/', views.Login),
    path('CarritoDeCompras/', views.CarritoDeCompras),
    path('Tienda/', views.Tienda),
    path('CrearUsuario/', views.CrearUsuario)
]